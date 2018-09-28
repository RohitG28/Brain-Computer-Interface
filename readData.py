import scipy.io as sio
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
from fft import plotFFT

data = sio.loadmat('S01E.mat')

## Following lists store the signal, trials, y and fs values for each subject separately
signals = []
trials = []
y = []
fs = []

for i in range(len(data['data'][0])):
	## transpose done to make channels as rows and time units as columns
	signals.append(np.transpose(data['data'][0][i][0][0][0]))
	trials.append(data['data'][0][i][0][0][1][0])
	trials[i] = np.append(trials[i],len(signals[i][0]))
	y.append(data['data'][0][i][0][0][2][0])
	fs.append(data['data'][0][i][0][0][3][0])

# pprint(signals)
## number of channels in the data
numChannels = len(signals[0])

## epochStart = portion to be left after the trial start
epochStart = 300

## epochEnd = portion to be left before the trial end
epochEnd = 0

## length of an epoch in ms
epochLen = 300

fig = plt.figure()

## extracts epochs for each subject
def epochExtractorPerSubject(signals, trials, y, epochs, epochClasses, epochLen, epochStart, epochEnd):
	for i in range(len(trials)-1):
		startTrial = trials[i]
		endTrial = trials[i+1]
		classValue = y[i]
		
		startPoint = startTrial + epochStart
		endPoint = startPoint + epochLen

		while True:
			if(endPoint > (endTrial-epochEnd)):
				break
			for i in range(numChannels):
				epochs[i].append(signals[i][startPoint:endPoint])

			epochClasses.append(classValue)
			startPoint = endPoint
			endPoint = startPoint + epochLen

	return epochs, epochClasses

def epochExtractor(signals, trials, y, epochLen, epochStart, epochEnd):
	epochs = []
	for i in range(numChannels):
		epochs.append([])

	epochClasses = []
	
	for i in range(len(signals)):
		epochs, epochClasses = epochExtractorPerSubject(signals[i],trials[i],y[i],epochs,epochClasses,epochLen,epochStart,epochEnd)

	return epochs, epochClasses

epochs, epochClasses = epochExtractor(signals, trials, y, epochLen, epochStart, epochEnd)

def visualizeSignalsForARecord(epochs, recordNum, epochClasses):
	xs = range(epochLen)
	color = 'b'
	if(epochClasses[recordNum] == 2):
		color = 'r'
	for i in range(numChannels):
		axes = fig.add_subplot(numChannels, 1, i+1)
		axes.plot(xs, epochs[i][recordNum], color)

def visualizeAllRecords(epochs, epochClasses):
	xs = range(epochLen)
	for i in range(numChannels):
		axes = fig.add_subplot(numChannels, 1, i+1)
		for j in range(len(epochClasses)):
			color = 'b'
			if(epochClasses[j] == 2):
				color = 'r'
			axes.plot(xs, epochs[i][j], color)

#### FFT
# plotFFT(epochs[1])

### To visualize the epochs
# visualizeAllRecords(epochs,epochClasses)
# plt.show()