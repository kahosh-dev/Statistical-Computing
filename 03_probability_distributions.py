"""
Topic 3: Probability Distributions
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
x = np.linspace(-4, 4, 300)
data = stats.norm.rvs(loc=0, scale=1, size=1000)

# Fit
mu, sigma = stats.norm.fit(data)
print(f"Fitted Normal: μ = {mu:.3f}, σ = {sigma:.3f}")

plt.figure(figsize=(8,5))
plt.hist(data, bins=30, density=True, alpha=0.6, label="Data")
plt.plot(x, stats.norm.pdf(x, mu, sigma), "r-", lw=2, label="Fitted Normal")
plt.title("Normal Distribution Fit")
plt.legend()
plt.savefig("../data/03_normal_fit.png")
plt.show()

# Binomial example
print("\nBinomial(n=10, p=0.3) P(X=3) =", stats.binom.pmf(3, 10, 0.3))
