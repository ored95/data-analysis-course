#!/usr/bin/env python3

from numpy.lib.function_base import hamming
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt
import scipy

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

dict = dict(zip('ACGT', range(4)))

def toint(x):
    return dict[x]

def get_features_and_labels(filename):
    dna = pd.read_csv(filename, sep='\t')
    features = np.empty(shape=(len(dna['X']), len(dna.loc[0, 'X'])), dtype=object)
    for i in range(len(dna['X'])):
        features[i] = np.array(list(map(toint, dna.loc[i, 'X'])))
    labels = dna['y']
    return features, labels

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def cluster_euclidean(filename):
    X, y = get_features_and_labels(filename)
    n_clusters = max(y) + 1
    model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='average')
    model.fit(X)
    perm = find_permutation(n_clusters, y, model.labels_)
    new_labels = [perm[label] for label in model.labels_]
    return accuracy_score(y, new_labels)

def cluster_hamming(filename):
    X, y = get_features_and_labels(filename)
    n_clusters = max(y) + 1
    model = AgglomerativeClustering(n_clusters=n_clusters, affinity='precomputed', linkage='average')
    distance_matrix = pairwise_distances(X, metric='hamming')
    plot(distance_matrix, affinity='precomputed')
    model.fit_predict(distance_matrix)
    perm = find_permutation(n_clusters, y, model.labels_)
    new_labels = [perm[label] for label in model.labels_]
    return accuracy_score(y, new_labels)

def main():
    # See more: https://en.wikipedia.org/wiki/Hierarchical_clustering
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
