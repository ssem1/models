import quandl
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show

from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split

import json

ticker1 = "WIKI/GOOG"
length1 = int(90)

def forecast(ticker, length):
    testdata = quandl.get(ticker)
    testdata = testdata[['Adj. Close']]

    forecast_out = length
    testdata['Prediction'] = testdata[['Adj. Close']].shift(-forecast_out)

    #print(testdata.tail())
    X = np.array(testdata.drop(['Prediction'], 1))
    X = preprocessing.scale(X)
    X_forecast = X[-forecast_out:]
    X = X[:-forecast_out]
    y = np.array(testdata['Prediction'])
    y = y[:-forecast_out]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

    clf = LinearRegression()
    clf.fit(X_train,y_train)

    confidence = clf.score(X_test, y_test)
    #print("confidence: ", confidence)
    forecast_prediction = clf.predict(X_forecast)
    #print(forecast_prediction)
    list_prediction = forecast_prediction.tolist()  # plots all columns against index
    plt.plot(list_prediction)
    #print(testdata)

    with open('data.json', 'w') as outfile:
        json.dump(list_prediction, outfile)
    # plt.show()
    return list_prediction
