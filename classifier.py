from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split
import numpy as np
from dimensionalityReduction import *

X = np.load("features.npy")
Y = np.load("classes.npy")

X = computePCA(X)

X_test, X_train, Y_test, Y_train = train_test_split(X, Y, test_size = 0.3, random_state = 109)

clf = svm.SVC(kernel = 'linear', C=100)
clf.fit(X_train, Y_train)

Y_pred = clf.predict(X_test)

print("Accuracy:",metrics.accuracy_score(Y_test, Y_pred))