import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()  # for plot styling
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import HashingVectorizer

''' Read in pickled data '''
pickle_path = '../../data_pickled/'
with open(pickle_path + 'session_dict_aug.pickle', 'rb') as handle:
    session_dict = pickle.load(handle)

data_vectorized = pd.DataFrame.from_dict(session_dict, orient='index').values

# KMeans
import pdb; pdb.set_trace()
K = 4
kmeans = KMeans(n_clusters=K)
kmeans.fit(data_vectorized)
y_kmeans = kmeans.predict(data_vectorized)

# PCA
pca = PCA(n_components=2)
data_vectorized = pca.fit_transform(data_vectorized)

plt.scatter(data_vectorized[:, 0], data_vectorized[:, 1], c=y_kmeans, s=50, cmap='viridis')
plt.show()
