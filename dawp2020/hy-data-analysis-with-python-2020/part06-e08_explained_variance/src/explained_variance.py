#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def explained_variance():
    df = pd.read_csv('src/data.tsv', sep='\t')
    pca = PCA(n_components=10)
    pca.fit(df)
    # plt.plot(df.columns, np.cumsum(pca.explained_variance_))
    plt.plot(np.arange(1, 11), np.cumsum(pca.explained_variance_))
    plt.show()
    return df.var(axis=1).values, pca.explained_variance_

def main():
    v, ev = explained_variance()
    print('The variances are:', ' '.join(['{:.3f}'.format(x) for x in v]))
    print('The explained variances after PCA are:', ' '.join(['{:.3f}'.format(x) for x in ev]))
    print(sum(v), sum(ev))

if __name__ == "__main__":
    main()
