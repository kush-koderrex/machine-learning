
# cart =Classsification and regrestion tree
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor


data=pd.read_csv("Salary_Data.csv")
# data.head()
data_x = data.iloc[:,:-1].values
data_y = data.iloc[:,-1].values

x_train,x_test,y_train,y_test=train_test_split(data_x,data_y,test_size=0.3,random_state=0)

reg=DecisionTreeRegressor(random_state=0)
reg.fit(x_train,y_train)
y_pred=reg.predict(x_test)
print(y_pred)
print(y_test)
reg=RandomForestRegressor(n_estimators=500,random_state=0)
reg.fit(x_train,y_train)
print(y_pred)
print(y_test)
x_grid=np.arange(min(data_x),max(data_x),0.01)
x_grid=x_grid.reshape((len(x_grid),1))
plt.plot(x_grid,reg.predict(x_grid),color="blue")
plt.scatter(data_x,data_y,color="red")
plt.title("Exp VS salary")
plt.xlabel("Exp")
plt.ylabel("Salary")
plt.show()
