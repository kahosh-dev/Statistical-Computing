"""
Topic 20: Bootstrap and Resampling Methods
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
data = np.random.normal(50, 10, 60)
n_boot = 5000
boot_means = [np.mean(np.random.choice(data, size=len(data), replace=True))
              for _ in range(n_boot)]

se = np.std(boot_means)
ci = np.percentile(boot_means, [2.5, 97.5])

print(f"Bootstrap SE of mean : {se:.3f}")
print(f"95% Bootstrap CI     : ({ci[0]:.2f}, {ci[1]:.2f})")

plt.hist(boot_means, bins=40, density=True, alpha=0.7)
plt.axvline(ci[0], color="r", linestyle="--")
plt.axvline(ci[1], color="r", linestyle="--")
plt.title("Bootstrap Distribution of the Mean")
plt.savefig("../data/20_bootstrap.png")
plt.show()
