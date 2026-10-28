"""
Topic 15: Data Transformation and Normalization
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

np.random.seed(42)
raw = np.random.exponential(scale=3, size=500).reshape(-1,1)

z = StandardScaler().fit_transform(raw)
mm = MinMaxScaler().fit_transform(raw)

fig, axes = plt.subplots(1,3, figsize=(12,4))
axes[0].hist(raw, bins=30); axes[0].set_title("Original")
axes[1].hist(z, bins=30); axes[1].set_title("Z-score (Standardized)")
axes[2].hist(mm, bins=30); axes[2].set_title("Min-Max Normalized")
plt.tight_layout()
plt.savefig("../data/15_transform.png")
plt.show()
