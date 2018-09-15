import scipy.io as sio
from pprint import pprint
import numpy as np

data = sio.loadmat('S01T.mat')

signals = []
trials = []
y = []
fs = []

for i in range(len(data['data'][0])):
	signals.append(np.transpose(data['data'][0][i][0][0][0]))
	trials.append(data['data'][0][i][0][0][1][0])
	trials[i] = np.append(trials[i],len(signals[i][0]))
	y.append(data['data'][0][i][0][0][2][0])
	fs.append(data['data'][0][i][0][0][3][0])

numChannels = len(signals[0])
epochStart = 300
epochEnd = 0
epochLen = 300

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
print(len(epochs),len(epochs[0]),len(epochClasses)) 