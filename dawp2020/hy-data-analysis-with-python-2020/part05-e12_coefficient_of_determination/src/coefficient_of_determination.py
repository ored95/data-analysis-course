import pandas as pd
from sklearn import linear_model
 
 
def coefficient_of_determination():
    scores = []
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    X = df.loc[:, "X1":"X5"]
    y = df.Y
 
    reg = linear_model.LinearRegression(fit_intercept=True)
 
    reg.fit(X, y)
    score = reg.score(X, y)
    scores.append(score)
 
    features = df.columns[:-1]
    print(features)
    for f in features:
        x = df[[f]]
        print(x.shape)
        reg.fit(x, y)
        scores.append(reg.score(x, y))
        
    return scores
    
def main():
    scores = coefficient_of_determination()
 
    z = scores[1:]
    for i in range(4):
        print(sum(z[i:i+2]))
        
    titles = "X X1 X2 X3 X4 X5".split()
    for title, score in zip(titles, scores):
        print(f"R2-score with feature(s) {title}: {score:.5f}")
 
if __name__ == "__main__":
    main()