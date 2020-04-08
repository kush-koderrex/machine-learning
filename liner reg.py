import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
data=pd.read_csv("Salary_Data.csv")
print(data.head(8))
data_x=data.iloc[:,:-1].values
data_y=data.iloc[:,-1].values
train_test_split()
