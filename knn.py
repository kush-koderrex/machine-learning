import pandas as pd

data=pd.read_csv("Social_Network_Ads.csv")
# print(data.head())
data_x=data.iloc[:,[2,3]].values
data_y=data.iloc[:,4].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.25, random_state=0)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
# print(X_test)
from sklearn.neighbors import KNeighborsClassifier
cls=KNeighborsClassifier(n_neighbors=5,metric="minkowski",p=2)
cls.fit(X_train,y_train)
y_pred=cls.predict(X_test)
# print(y_pred)
# print("actual value")
# print(y_test)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print(cm)
from sklearn.metrics import accuracy_score
ac=accuracy_score(y_test,y_pred)
print(ac)