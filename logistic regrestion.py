import pandas as pd
data=pd.read_csv("Social_Network_Ads.csv")
data_x=data.iloc[:,[2,3]].values
data_y=data.iloc[:,4].values
# print(data.head())
print(data.tail())
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.25, random_state=0)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
from sklearn.linear_model import LogisticRegression
cls=LogisticRegression(random_state=0)
cls.fit(X_train,y_train)
cls.fit(X_train,y_train)
y_pred=cls.predict(X_test)
print(y_pred)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print(cm)
from sklearn.metrics import accuracy_score
ac=accuracy_score(y_test,y_pred)
print(ac)