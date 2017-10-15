#coding=utf-8
# Required Packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

def main():
    pass

def get_data(file_name):
    data = pd.read_csv(file_name)

    return data
    # X_parameter = []
    # Y_parameter = []
    # for single_square_feet ,single_price_value in zip(data['square_feet'],data['price']):
    #     X_parameter.append([float(single_square_feet)])
    #     Y_parameter.append(float(single_price_value))
    # return X_parameter,Y_parameter

data = get_data("data/pm25_train.csv")
X = data[['date','hour','DEWP','TEMP','PRES','Iws','Is','Ir','cbwd_NE','cbwd_NW','cbwd_SE','cbwd_cv','pm2.5']]
Y = data['pm2.5']

date = X['date'].copy()
month = np.zeros(X.shape[0])
day = np.zeros(X.shape[0])
for i,val in enumerate(date):
    month[i] = int(val[5:7])
    day[i] = int(val[8:])
X.insert(13,'month',month)
X.insert(14,'day',day)


plt.subplot(3,1,1)
plt.xlabel("PRES")
plt.ylabel("pm2.5")
t1 = X[['PRES','pm2.5']].groupby('PRES').mean()
plt.scatter(t1.index,t1['pm2.5'])
# plt.scatter(X['PRES'],Y)


plt.subplot(3,1,2)
plt.xlabel("DEWP")
plt.ylabel("pm2.5")
t1 = X[['DEWP','pm2.5']].groupby('DEWP').mean()
plt.scatter(t1.index,t1['pm2.5'])

plt.subplot(3,1,3)
plt.xlabel("TEMP")
plt.ylabel("pm2.5")
t2 = X[['TEMP','pm2.5']].groupby('TEMP').mean()
plt.scatter(t2.index,t2['pm2.5'])

plt.subplots_adjust(hspace=0.5)

plt.show()


if __name__ == '__main__':
  main()