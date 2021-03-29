#!/usr/bin/env python3

from collections import Counter
from inspect import getfile
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=list(map(lambda s: s.rstrip(), data.readlines()))
    return lines

def get_features(a):
    na = np.empty(shape=(len(a), len(alphabet)), dtype=object)
    for i in range(na.shape[0]):
        na[i] = (np.array([a[i].count(x) for x in alphabet]))
    return na

def contains_valid_chars(s):
    return np.all([x in alphabet for x in s])   # np.isin(s, alphabet) not work?!

def get_features_and_labels():
    finW, engW = load_finnish(), load_english()
    # Convert the Finnish words to lowercase, and then filter out 
    # those words that contain characters that don’t belong to the alphabet.
    finW = list(map(str.lower, finW))
    finW = list(filter(contains_valid_chars, finW))
    # For the English words first filter out those words that begin with an uppercase 
    # letter to get rid of proper nouns. Then proceed as with the Finnish words.
    engW = list(filter(lambda w: w[0] not in alphabet[:-3].upper(), engW))
    engW = list(map(str.lower, engW))
    engW = list(filter(contains_valid_chars, engW))
    print(len(engW))
    # Generate features and labels
    labels   = np.concatenate([np.zeros(shape=len(finW), dtype=int), np.ones(shape=len(engW), dtype=int)], axis=0)
    features = get_features(np.concatenate([finW, engW], axis=0))
    return features, labels

def word_classification():
    features, labels = get_features_and_labels()
    model = MultinomialNB()
    # See more: https://scikit-learn.org/stable/modules/cross_validation.html
    # https://scikit-learn.org/stable/tutorial/statistical_inference/model_selection.html
    kf = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    scores = cross_val_score(model, features, labels, cv=kf, n_jobs=-1)
    return scores

def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
