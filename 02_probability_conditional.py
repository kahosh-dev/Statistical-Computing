"""
Topic 2: Probability and Conditional Probability
"""
import numpy as np

np.random.seed(42)
# Simulate a medical test
# Disease prevalence 1%, sensitivity 95%, specificity 90%
n = 100_000
disease = np.random.rand(n) < 0.01
positive = np.where(disease,
                    np.random.rand(n) < 0.95,   # true positive
                    np.random.rand(n) < 0.10)   # false positive

p_disease = disease.mean()
p_pos = positive.mean()
p_disease_given_pos = (disease & positive).sum() / positive.sum()

print(f"P(Disease)                = {p_disease:.4f}")
print(f"P(Positive)               = {p_pos:.4f}")
print(f"P(Disease | Positive)     = {p_disease_given_pos:.4f}")

# Theoretical Bayes
prior = 0.01
sens, spec = 0.95, 0.90
bayes = (sens*prior) / (sens*prior + (1-spec)*(1-prior))
print(f"Bayes theorem result      = {bayes:.4f}")

print("\nInterpretation: Even with a positive test, the probability of disease "
      "is only ~8–9% because the disease is rare (base-rate effect).")
