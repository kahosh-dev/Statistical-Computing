"""
Topic 19: Non-parametric Statistical Methods
"""
import numpy as np
from scipy import stats

np.random.seed(42)
# Two independent samples (non-normal)
a = np.random.exponential(2, 40)
b = np.random.exponential(3, 40)

# Mann-Whitney U
u_stat, p_u = stats.mannwhitneyu(a, b, alternative="two-sided")
print(f"Mann-Whitney U statistic: {u_stat:.1f}, p = {p_u:.4f}")

# Wilcoxon signed-rank (paired)
diff = a - np.random.permutation(b)[:40]
w_stat, p_w = stats.wilcoxon(diff)
print(f"Wilcoxon statistic      : {w_stat:.1f}, p = {p_w:.4f}")
