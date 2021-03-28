#!/usr/bin/env python3

from numpy.lib.function_base import select
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import scipy

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def nonconvex_clusters():
    df = pd.read_csv('src/data.tsv', sep='\t')
    n_labels = len(np.unique(df['y']))
    
    result = []
    for eps in np.arange(0.05, 0.2, 0.05):
        X, y = df[df.columns[:2]], df['y']
        model = DBSCAN(eps, n_jobs=-1)
        model.fit(X)
        
        selection = np.where(model.labels_ != -1)[0]
        n_outlier = len(y) - len(selection)
        if n_outlier > 0:
            X = X.loc[selection, :]
            y = y[selection]
            model.fit(X)
        
        n_cluster = len(np.unique(model.labels_))
        if n_labels == n_cluster:
            perm = find_permutation(n_cluster, y, model.labels_)
            new_labels = [perm[label] for label in model.labels_]
            score = accuracy_score(y, new_labels)
        else:
            score = np.nan

        result.append([eps, score, n_cluster, n_outlier])

    table = pd.DataFrame(np.array(result))
    table.columns = ["eps", "Score", "Clusters", "Outliers"]
    return table

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
