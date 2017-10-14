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

data = get_data("pm25_train.csv")
X = data[['hour','DEWP','TEMP','PRES','Iws','Is','Ir','cbwd_NE','cbwd_NW','cbwd_SE','cbwd_cv']]
Y = data['pm2.5']
plt.scatter(X['hour'],Y)

if __name__ == '__main__':
  main()