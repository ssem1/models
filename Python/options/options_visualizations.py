import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show

import csv

Strike_Prices = []
ITM_Call = []
ATM_Call = []
OTM_Call = []

df = pd.read_csv('OptionPrices.csv')
print(df.keys())
Strike_Prices = df.Strike
ITM_Call = df.ITM
ATM_Call = df.ATM
OTM_Call = df.OTM
OTM_Put = df.OTMP
ATM_Put = df.ATMP
ITM_Put = df.ITMP
strangle = OTM_Call + OTM_Put
straddle = ATM_Call + ATM_Put
xaxis = np.arange(1,42)
# output to static HTML file
output_file("Calls.html")

c = figure(title="Compare Calls", x_axis_label='Stock Price', y_axis_label='Profit', width = 800)

c.line(xaxis, ITM_Call, color='#A7414A', legend="ITM Call", line_width=3)
c.line(xaxis, ATM_Call, color='#282726', legend="ATM Call", line_width=3)
c.line(xaxis, OTM_Call, color='#6A8A82', legend="OTM Call", line_width=3)

p = figure(title="Compare Puts", x_axis_label='Stock Price', y_axis_label='Profit', width = 800)

p.line(xaxis, OTM_Put, color='#6C6B74', legend="OTM Put", line_width=3)
p.line(xaxis, ATM_Put, color='#2E303E', legend="ATM Put", line_width=3)
p.line(xaxis, ITM_Put, color='#9199BE', legend="ITM Put", line_width=3)

stran = figure(title="Strangle", x_axis_label='Stock Price', y_axis_label='Profit', width = 800)

stran.line(xaxis, OTM_Call, color='#F29D4B', legend="OTM Put", line_width=3)
stran.line(xaxis, OTM_Put, color='#D57030', legend="OTM Put", line_width=3)
stran.line(xaxis, strangle, color='#8B281F', legend="Strangle", line_width=3)

strad = figure(title="Straddle", x_axis_label='Stock Price', y_axis_label='Profit', width = 800)

strad.line(xaxis, ATM_Call, color='#6441a5', legend="ATM Call", line_width=3)
strad.line(xaxis, ATM_Put, color='#657786', legend="ATM Put", line_width=3)
strad.line(xaxis, straddle, color='#355ebe', legend="Straddle", line_width=3)

# show the results
#show(c)
#show(p)
#show(stran)
show(strad)
