"""
Topic 7: Correlation and Covariance
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
x = np.random.normal(0, 1, 100)
y = 0.7*x + np.random.normal(0, 0.7, 100)
df = pd.DataFrame({"X": x, "Y": y})

print("Covariance matrix:\n", df.cov().round(3))
print("\nCorrelation matrix:\n", df.corr().round(3))

sns.scatterplot(x="X", y="Y", data=df)
plt.title("Scatter plot (r ≈ 0.7)")
plt.savefig("../data/07_scatter.png")
plt.show()
