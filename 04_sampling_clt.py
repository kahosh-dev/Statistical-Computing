"""
Topic 4: Sampling Distributions and Central Limit Theorem
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
# Highly skewed population (Exponential)
pop = np.random.exponential(scale=2, size=100_000)

def sample_means(n, n_samples=2000):
    return [np.mean(np.random.choice(pop, n)) for _ in range(n_samples)]

fig, axes = plt.subplots(1, 3, figsize=(12,4))
for ax, n in zip(axes, [5, 30, 100]):
    means = sample_means(n)
    ax.hist(means, bins=40, density=True, alpha=0.7)
    ax.set_title(f"n = {n}\nSE ≈ {np.std(means):.3f}")
plt.suptitle("CLT: Sampling Distribution of the Mean")
plt.tight_layout()
plt.savefig("../data/04_clt.png")
plt.show()

print("Interpretation: As sample size increases the sampling distribution "
      "becomes closer to Normal and the standard error decreases.")
