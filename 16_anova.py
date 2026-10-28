"""
Topic 16: ANOVA and Experimental Design
"""
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

np.random.seed(42)
group_a = np.random.normal(20, 3, 30)
group_b = np.random.normal(22, 3, 30)
group_c = np.random.normal(25, 3, 30)

df = pd.DataFrame({
    "value": np.concatenate([group_a, group_b, group_c]),
    "group": ["A"]*30 + ["B"]*30 + ["C"]*30
})

model = ols("value ~ C(group)", data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

# Post-hoc (Tukey)
from statsmodels.stats.multicomp import pairwise_tukeyhsd
print("\nTukey HSD:")
print(pairwise_tukeyhsd(df["value"], df["group"]))
