#!/usr/bin/env python3
 
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
 
import scipy
def find_permutation(real_labels, labels):
    """
    Modifed version: renaming the clusters
    """
    permutation=[]
    m=max(labels)
    for i in range(m+1):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation
 
def nonconvex_clusters():
    df = pd.read_csv("src/data.tsv", sep="\t")
    X = df.loc[:, "X1":"X2"].values
    y = df.y.values
    result = []
    for e in np.arange(0.05, 0.2, 0.05):
        model=DBSCAN(e)
        model.fit(X)
        idx = model.labels_ == -1
        outliers = np.sum(idx)
        clusters = max(model.labels_) + 1
        if clusters == 2:
            permutation = find_permutation(y, model.labels_)
            acc = accuracy_score(y[~idx], [ permutation[label] for label in model.labels_[~idx]])
        else:
            acc = np.nan
        result.append([e, acc, clusters, outliers])
    df2 = pd.DataFrame(np.array(result))
    df2.columns = ["eps", "Score", "Clusters", "Outliers"]
    return df2
 
def main():
    print(nonconvex_clusters())
 
if __name__ == "__main__":
    main()
 