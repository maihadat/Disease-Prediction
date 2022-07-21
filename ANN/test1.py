from cv2 import kmeans
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.cluster import KMeans
sc = MinMaxScaler()


df = pd.read_csv("./out.csv")
df.drop(['Unnamed: 0'], inplace=True, axis=1)
print("dframe", df)
print("label", df['Disease'].value_counts())
print("num label", len(df['Disease'].unique()))
#map 
label_list = df['Disease'].unique()
label_map = dict([(label_list[i], i) for i in range(len(label_list))])
print(label_map)
df['Disease'] = df['Disease'].map(label_map)

# #fit
X = df.iloc[:, :-1].values
y = df['Disease'].values
X = sc.fit_transform(X)
# y = sc.fit_transform(y.reshape(-1, 1))
X_train, X_test, y_train, y_test = train_test_split(X[:, :3], y, stratify=y, test_size=0.9, random_state=4)
print("data",  X_train.shape, y_train.shape)

nnb = GridSearchCV(KNeighborsClassifier(), param_grid={'n_neighbors' : [i + 1 for i in range(20)]})
nnb.fit(X_train, y_train)
print("Label", y_train)
y_pred = nnb.predict(X_test)
print(f"accuracy of {nnb.best_estimator_}", (y_pred == y_test).sum()/y_test.shape[0])


# kmeans = KMeans(n_clusters=len(label_list))
# kmeans.fit(X_train, y_train)
# print("Label", y_train)
# y_pred = kmeans.predict(X_test)
# print(f"accuracy", (y_pred == y_test).sum()/y_test.shape[0])

# #eda
# print("main df", len(df))
# print("class 0", len(df.loc[(df['itching'] != 0) & (df['Disease'] == 6)]))