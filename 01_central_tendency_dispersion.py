"""
Topic 1: Measures of Central Tendency and Dispersion
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
# Synthetic exam scores
scores = np.random.normal(68, 12, 200).clip(0, 100)
df = pd.DataFrame({"score": scores})

print("=== Summary Statistics ===")
print(df["score"].describe())
print(f"\nMode (approx): {df['score'].mode().values[0]:.1f}")
print(f"Variance     : {df['score'].var():.2f}")
print(f"IQR          : {df['score'].quantile(0.75) - df['score'].quantile(0.25):.2f}")

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
sns.histplot(df["score"], kde=True)
plt.title("Histogram of Scores")
plt.subplot(1,2,2)
sns.boxplot(y=df["score"])
plt.title("Boxplot of Scores")
plt.tight_layout()
plt.savefig("../data/01_boxplot_hist.png")
plt.show()

print("\nInterpretation: Mean ≈ Median → roughly symmetric distribution. "
      "Boxplot shows median, IQR and possible outliers.")
