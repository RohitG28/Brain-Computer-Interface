from keras.models import Sequential
from keras.layers import Dense,Activation
import numpy as np
import matplotlib.pyplot as plt

X = np.load("features.npy")
Y = np.load("classes.npy")
inputShape = len(X)

model = Sequential()
model.add(Dense(12, input_dim = inputShape, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

model.compile(loss='mean_squared_error', optimizer = 'sgd', metrics = ['accuracy'])
# plot_loss_callback = LambdaCallback(on_epoch_end=lambda epoch, logs: plt.plot(np.arange(epoch), logs['loss']))
history = model.fit(X, Y, epochs=50, validation_split=0.25, batch_size=10)

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()