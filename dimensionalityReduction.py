import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# x = np.load("features.npy")
# y = np.load("classes.npy")

def computePCA(x):
	x = StandardScaler().fit_transform(x)
	pca = PCA(n_components=50)
	principalComponents = pca.fit_transform(x)
	return principalComponents