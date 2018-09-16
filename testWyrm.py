import numpy as np
import scipy.io as sio
from pprint import pprint
import matplotlib.pyplot as plt
from wyrm.types import Data
from wyrm import processing as proc 

dataArr = []

data = sio.loadmat('S02E.mat')

## Following lists store the signal, trials, y and fs values for each subject separately
signals = []
trials = []
y = []
fs = []

for i in range(len(data['data'][0])):
    # transpose done to make channels as rows and time units as columns
    signals.append(np.transpose(data['data'][0][i][0][0][0]))
    trials.append(data['data'][0][i][0][0][1][0])
    trials[i] = np.append(trials[i],len(signals[i][0]))
    y.append(data['data'][0][i][0][0][2][0])
    fs.append(data['data'][0][i][0][0][3][0])

    continuousData = data['data'][0][i][0][0][0]
    times = range(len(signals[i][0]))
    channels = range(1, len(signals[i]) + 1)
    axes = [times, channels]
    names = ['time', 'channels']
    units = ['ms', '#']
    dataArr.append(Data(continuousData, axes, names, units))

pprint(dataArr[0])
