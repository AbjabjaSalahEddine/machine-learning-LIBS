import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def make_model():
    with open('model/valeurs.csv') as f:
        results = np.genfromtxt(f, delimiter=';')
    for i in range(len(results)):
        results[i][-1]=results[i][-1]*10000
    print(results)
    results = np.delete(results,0,1)
    results = np.delete(results,0,0)
    print(results)
    Y=np.zeros((len(results)*4,len(results[0])),float)
    for i in range(len(Y)):
        Y[i]=results[i//4]
    #Y=np.delete(Y,-1,0)
    with open('model/recap.csv', 'r') as f_in:
        echantils = np.genfromtxt('model/recap.csv', delimiter=';')
    echantils = np.delete(echantils,0,1)
    echantils = echantils[1:len(echantils)-4]
    print(echantils)
    X=echantils.transpose()
    #X=np.delete(X,-1,0)
    linear_regressor = LinearRegression()  
    linear_regressor.fit(X, Y)  
    return linear_regressor

