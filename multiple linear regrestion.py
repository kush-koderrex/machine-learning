import pandas as pd
data= pd.read_csv("taxi.csv")
print(data.head())
data_x=data.iloc[:,:-1].values
data_y=data.iloc[:,-1].values
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(data_x,data_y,test_size=0.3,random_state=0)
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(x_train,x_test)
y_pred=reg.predict(x_test)
print(y_pred)



