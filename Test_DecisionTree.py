
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv("Data_sets/out.csv")
df2 = pd.read_csv("Data_sets/Testing.csv")

X = df.iloc[:, 1:-1]
Y = df.iloc[:, -1]

X_train, X_app, Y_train, Y_app = train_test_split(X, Y, test_size=1000, random_state=50)

tree = DecisionTreeClassifier()
tree.fit(X_train, Y_train)

print(tree.score(X_app, Y_app)*100)

