"""
Topic 12: Random Numbers and Monte Carlo Methods
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
N = 50_000
# Estimate π by Monte Carlo
x, y = np.random.uniform(-1, 1, (2, N))
inside = x**2 + y**2 <= 1
pi_est = 4 * inside.mean()
print(f"Monte Carlo estimate of π: {pi_est:.5f}")

running = 4 * np.cumsum(inside) / np.arange(1, N+1)
plt.plot(running)
plt.axhline(np.pi, color="r", linestyle="--", label="True π")
plt.xlabel("Samples"); plt.ylabel("Estimate"); plt.legend()
plt.title("Monte Carlo Convergence for π")
plt.savefig("../data/12_mc_pi.png")
plt.show()
