import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.neighbors import LocalOutlierFactor
import csv

s = []
# Sample data ----
with open('AMD.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        s.append(row[0])
s = [float(i) for i in s]
print(s)

x = 1
totaldowndays = 0
totalupdays = 0
bigdowndays = 0
bigupdays = 0
level_change = 0.05

while x < len(s)-1:
    if ((s[x] / s[x+1]) > 1+level_change) or ((s[x] / s[x+1]) < 1-level_change):
        print("Anomaly on position " + str(x) + " of " + str(round(100-((s[x] / s[x+1])*100),2)) + "%")
        if(100-((s[x] / s[x+1])*100)) > 0:
            bigupdays+=1
        if(100-((s[x] / s[x+1])*100)) < 0:
            bigdowndays+=1
    if(100-((s[x] / s[x+1])*100)) > 0:
        totalupdays+=1
    if(100-((s[x] / s[x+1])*100)) < 0:
        totaldowndays+=1
    x+=1

print("total number of days in the green: " + str(totalupdays))
print("total number of days in the red: " + str(totaldowndays))
print("total number of days deep in the green: " + str(bigupdays))
print("total number of days deep in the red: " + str(bigdowndays))
print("Yesterday saw an increase of 5.41%")
