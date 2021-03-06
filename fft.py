import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import stft

def plotFFT(signal):
	Fs = 150.0;  # sampling rate
	Ts = 1.0/Fs; # sampling interval

	t = range(len(signal))

	n = len(signal) # length of the signal
	k = np.arange(n)
	T = n/Fs
	frq = k/T # two sides frequency range
	frq = frq[range(n/2)] # one side frequency range

	Y = np.fft.fft(signal)/n # fft computing and normalization
	Y = Y[range(n/2)]

	fig, ax = plt.subplots(2, 1)
	ax[0].plot(t,signal)
	ax[0].set_xlabel('Time')
	ax[0].set_ylabel('Amplitude')
	ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
	ax[1].set_xlabel('Freq (Hz)')
	ax[1].set_ylabel('|Y(freq)|')

	plt.show()

def stftCalculation(epochs, windowSize = 64):
	epochs = np.transpose(epochs, (1,0,2))
	images = []
	for i in range(len(epochs)):
		singleImage = []
		for j in range(len(epochs[0])):
			_,_,z = stft(epochs[i][j], nperseg = windowSize)
			singleImage.append(z)

		images.append(np.concatenate(singleImage))
	images = np.array(images)
	return images