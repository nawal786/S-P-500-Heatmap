'''
N. Valliani
11/2020

S&P500 data since 1970 visualized
'''

import pandas as pd
import sys
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt

sp_df = pd.read_csv("sp500.csv")    # Open CSV File

# Drop un-needed columns
sp_df = sp_df.drop("Price",axis=1)
sp_df = sp_df.drop("High",axis=1)
sp_df = sp_df.drop("Low",axis=1)
sp_df = sp_df.drop("Volume",axis=1)
sp_df = sp_df.drop("Open",axis=1)

# Cast data as required types (year as ints, percent changes as floats)
sp_df["Year"] = sp_df["Year"].astype(int)
sp_df["Percent Change"] = sp_df["Percent Change"].astype(float)

# Create the heatmap data object
heatmap_data = pd.pivot_table(sp_df, values="Percent Change", index="Month", columns="Year")
ax = plt.axes()

# Create heatmap
# xticklables and yticklabels = True to show all data on both axes
# vmax and vmin symmetrical with the center set at 0.
# annot can be set to True, but the map gets crowded so it is set to false
sns.heatmap(heatmap_data,xticklabels=True, yticklabels=True,cmap="RdBu",ax=ax,vmax=25,vmin=-25,center=0,annot=False)
ax.set_title("S&P500 Percent Change Every Month Since 1970")
plt.show()

# enjoy