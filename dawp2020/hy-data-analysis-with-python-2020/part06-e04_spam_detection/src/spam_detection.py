#!/usr/bin/env python3
import gzip
import numpy as np
import sklearn      # just for TMC 
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

def spam_detection(random_state=0, fraction=1.0):
    # Read the lines from these files into arrays by using gzip.open()
    with gzip.open('src/ham.txt.gz', 'r') as fh:
        ham = list(map(lambda s: s.rstrip(), fh.readlines()))
    with gzip.open('src/spam.txt.gz', 'r') as fs:
        spam = list(map(lambda s: s.rstrip(), fs.readlines()))
    
    # Note: The tests use the 'fraction' parameter with value 0.1 to ease to load 
    # on the TMC server. If full data were used and the solution did something non-optimal, 
    # it could use huge amounts of memory, causing the solution to fail.
    ham = ham[:int(fraction * len(ham))]
    spam = spam[:int(fraction * len(spam))]

    # Labels
    labels = np.hstack([[0]*len(ham), [1]*len(spam)])

    # Features
    # Forms the combined feature matrix using CountVectorizer class’ fit_transform method.
    # See more: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
    mails = np.hstack([ham, spam])
    vectorizer = CountVectorizer()
    mails = vectorizer.fit_transform(mails)

    # Naive-Bayer Classification
    model = MultinomialNB()
    X_train, X_test, y_train, y_test = train_test_split(mails, labels, train_size=0.75, random_state=random_state)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    return score, len(y_test), int((1-score) * len(y_test))

def main():
    accuracy, total, misclassified = spam_detection(random_state=5, fraction=0.1)
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
