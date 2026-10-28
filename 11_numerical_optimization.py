"""
Topic 11: Numerical Optimization
"""
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def rosenbrock(x):
    return (1 - x[0])**2 + 100*(x[1] - x[0]**2)**2

res = minimize(rosenbrock, x0=[-1, 1], method="BFGS")
print("Success:", res.success)
print("Optimum x :", res.x.round(5))
print("Function value:", res.fun)

# Contour plot
x = np.linspace(-2, 2, 200)
y = np.linspace(-1, 3, 200)
X, Y = np.meshgrid(x, y)
Z = (1-X)**2 + 100*(Y-X**2)**2
plt.contour(X, Y, Z, levels=np.logspace(-1, 3, 20))
plt.plot(res.x[0], res.x[1], "r*", markersize=15, label="Optimum")
plt.legend(); plt.title("Rosenbrock Function Optimization")
plt.savefig("../data/11_optim.png")
plt.show()
