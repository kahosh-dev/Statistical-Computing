"""
Topic 6: Hypothesis Testing
"""
import numpy as np
from scipy import stats

np.random.seed(42)
# One-sample t-test: H0: μ = 100
sample = np.random.normal(103, 10, 30)
t_stat, p_val = stats.ttest_1samp(sample, 100)

print(f"t-statistic : {t_stat:.3f}")
print(f"p-value     : {p_val:.4f}")
print("Decision    :", "Reject H0" if p_val < 0.05 else "Fail to reject H0")
print("\nInterpretation: If p < 0.05 we have evidence that the true mean "
      "differs from 100.")
