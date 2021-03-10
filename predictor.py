import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def prediction(path,lr):
    with open(path) as f:
        spectre = np.genfromtxt(f, delimiter=';')
    spectre=spectre[1:2045]
    print(spectre)
    return lr.predict([spectre])
#prediction("C:/Users/lenovo/Desktop/spectre.csv")

def spectre(path):
    with open(path) as f:
        spectre = np.genfromtxt(f, delimiter=';')
    spectre=spectre[1:2045]
    X=np.arange(1,2045)
    return [spectre,X]
