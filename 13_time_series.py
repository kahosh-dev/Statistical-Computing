"""
Topic 13: Time-series Analysis
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

np.random.seed(42)
dates = pd.date_range("2020-01-01", periods=120, freq="M")
trend = np.linspace(10, 30, 120)
season = 5 * np.sin(np.arange(120)*2*np.pi/12)
noise = np.random.normal(0, 1.5, 120)
ts = pd.Series(trend + season + noise, index=dates)

decomp = seasonal_decompose(ts, model="additive", period=12)

fig = decomp.plot()
fig.set_size_inches(10, 8)
plt.savefig("../data/13_timeseries.png")
plt.show()
print("Interpretation: Clear upward trend and yearly seasonality visible after decomposition.")
