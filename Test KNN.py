import numpy as np
import pandas as pd
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("Data_sets/out.csv")
array = df.to_numpy()

X = array[:, 1:-1]
Y = array[:, -1]

X_train, X_app, Y_train, Y_app = train_test_split(X, Y, test_size=600)

# KNN with 10 nearest datapoints
clf = neighbors.KNeighborsClassifier(n_neighbors=10, p=2)
clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_app)
print(accuracy_score(Y_app, Y_pred) * 100)


