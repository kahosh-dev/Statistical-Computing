"""
Topic 17: Chi-square and Categorical Data Analysis
"""
import numpy as np
from scipy.stats import chi2_contingency

# Contingency table: Treatment vs Recovery
table = np.array([[40, 10],
                  [30, 20]])
print("Observed:\n", table)

chi2, p, dof, expected = chi2_contingency(table)
print(f"\nChi-square statistic: {chi2:.3f}")
print(f"p-value             : {p:.4f}")
print(f"Degrees of freedom  : {dof}")
print("Expected frequencies:\n", expected.round(2))
print("\nConclusion:", "Reject independence" if p < 0.05 else "No evidence against independence")
