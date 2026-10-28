"""
Topic 22: Missing-data Analysis and Imputation
"""
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.DataFrame({
    "A": np.random.normal(10, 2, 100),
    "B": np.random.normal(20, 5, 100),
    "C": np.random.normal(5, 1, 100)
})
# Introduce missingness
mask = np.random.rand(*df.shape) < 0.15
df_missing = df.mask(mask)

print("Missing counts:\n", df_missing.isna().sum())
print("\n% missing:\n", (df_missing.isna().mean()*100).round(1))

imputer = SimpleImputer(strategy="mean")
df_imp = pd.DataFrame(imputer.fit_transform(df_missing), columns=df.columns)

print("\nMean before imputation (complete cases only):")
print(df_missing.mean().round(2))
print("Mean after mean-imputation:")
print(df_imp.mean().round(2))
