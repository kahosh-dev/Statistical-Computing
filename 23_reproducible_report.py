"""
Topic 23: Statistical Reporting and Reproducible Analysis
This script itself is a minimal reproducible report.
In practice use Jupyter Notebook or Quarto / R Markdown.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(123)
data = np.random.normal(75, 10, 50)

print("="*50)
print("REPRODUCIBLE STATISTICAL REPORT")
print("="*50)
print(f"Sample size     : {len(data)}")
print(f"Sample mean     : {np.mean(data):.2f}")
print(f"Sample SD       : {np.std(data, ddof=1):.2f}")
print(f"95% CI          : {stats.t.interval(0.95, len(data)-1, loc=np.mean(data), scale=stats.sem(data))}")

plt.hist(data, bins=12, edgecolor="k", alpha=0.7)
plt.title("Distribution of Sample")
plt.xlabel("Value"); plt.ylabel("Frequency")
plt.savefig("../data/23_report_hist.png")
plt.show()

print("\nConclusion: The sample appears roughly normal. "
      "All code, data generation and results are contained in this single script, "
      "making the analysis fully reproducible.")
