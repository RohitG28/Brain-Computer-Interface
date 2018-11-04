from keras.models import Sequential
from keras.layers import Dense,Activation
import numpy as np
import matplotlib.pyplot as plt

X = np.load("features.npy")
Y = np.load("classes.npy")
inputShape = np.shape(X)[1]

model = Sequential()
model.add(Dense(25, input_dim = inputShape, activation = 'sigmoid'))
model.add(Dense(50, activation = 'sigmoid'))
model.add(Dense(10, activation = 'sigmoid'))
model.add(Dense(5, activation = 'sigmoid'))
# model.add(Dense(50, activation = 'sigmoid'))
# model.add(Dense(25, activation = 'sigmoid'))
model.add(Dense(1, activation = 'sigmoid'))

model.compile(loss='mean_squared_error', optimizer = 'adam', metrics = ['accuracy'])
history = model.fit(X, Y, epochs=100, validation_split=0.25, batch_size=10)

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()