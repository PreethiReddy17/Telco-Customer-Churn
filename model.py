import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import warnings
import pickle
warnings.filterwarnings('ignore')
import math

data=pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
data=np.array(data)
X=data[['Contract', 'MonthlyCharges', 'TotalCharges', 'tenure_group']]
Y=data[['Churn']]
X=X.astype('int')
Y=Y.astype('int')

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=0)
model1=LogisticRegression(max_iter=5000)
model1.fit(X_train,Y_train)

pickle.dump(model1,open(r"C:\Users\KEERTHI REDDY\churn.pkl", "wb"))
model= pickle.load(open(r"C:\Users\KEERTHI REDDY\churn.pkl", "rb"))