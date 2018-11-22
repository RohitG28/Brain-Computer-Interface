from keras.models import Sequential
from keras.layers import Dense,Activation,Conv2D,MaxPooling2D
import numpy as np
import matplotlib.pyplot as plt

X = np.load("imageFeatures.npy")
Y = np.load("classes.npy")
inputShape = np.shape(X)

model = Sequential()
model.add(Conv2D(6, kernel_size = (3,3),input_dim = inputShape, activation = 'relu'))
model.add(MaxPooling2D((2,2)))
model.add(Conv2D(12, kernel_size = (3,3), activation = 'relu'))
model.add(MaxPooling2D((2,2)))
model.add(Dense(100, activation = 'relu'))
model.add(Dense(2, activation = 'softmax'))

model.compile(loss='categorical_crossentropy', optimizer = 'sgd', metrics = ['accuracy'])
# plot_loss_callback = LambdaCallback(on_epoch_end=lambda epoch, logs: plt.plot(np.arange(epoch), logs['loss']))
history = model.fit(X, Y, epochs=50, validation_split=0.25, batch_size=10)

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()