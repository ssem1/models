import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import json

from fbprophet import Prophet

import pyEX as p

start = datetime(2014,1,1)
end = datetime.today()
ticker = 'AMD'
timeframe = '5y'
# n = number of periods/number of days
N = 365

def Predict(ticker, timeframe, N):
    df = p.chartDF(ticker, timeframe)
    df = df[['close']]
    df.reset_index(level=0, inplace=True)
    df.columns=['ds','y']
    m = Prophet()
    m.fit(df)
    future = m.make_future_dataframe(periods=N)
    forecast = m.predict(future)
    forecast['day_week'] = forecast.ds.dt.weekday_name
    forecast = forecast[forecast.day_week != 'Sunday']
    forecast = forecast[forecast.day_week != 'Saturday']
    #trend = forecast['trend'].tolist()
    #print(forecast)
    #print(trend)
    #print(forecast)
    #m.plot(forecast,xlabel='Date', ylabel='Price')
    #m.plot_components(forecast)
    #plt.show()
    return forecast
Predict(ticker, timeframe, N)
