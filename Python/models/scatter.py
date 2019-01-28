import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the amd dataset
df = pd.read_csv("file_path.csv")
df.plot()  # plots all columns against index
df.plot(kind='scatter',x='x',y='y') # scatter plot
df.plot(kind='density')  # estimate density function
