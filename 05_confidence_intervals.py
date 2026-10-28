"""
Topic 5: Confidence Intervals
"""
import numpy as np
from scipy import stats

np.random.seed(42)
data = np.random.normal(loc=50, scale=8, size=40)
n, mean, se = len(data), np.mean(data), stats.sem(data)
ci = stats.t.interval(0.95, df=n-1, loc=mean, scale=se)

print(f"Sample mean          : {mean:.2f}")
print(f"95% CI               : ({ci[0]:.2f}, {ci[1]:.2f})")
print("\nInterpretation: We are 95% confident that the true population mean "
      "lies between the lower and upper limits of the interval.")
