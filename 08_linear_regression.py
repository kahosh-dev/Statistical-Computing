"""
Topic 8: Linear Regression and Least Squares
"""
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

np.random.seed(42)
X = np.random.uniform(0, 10, 80)
y = 3 + 1.5*X + np.random.normal(0, 2, 80)

X_const = sm.add_constant(X)
model = sm.OLS(y, X_const).fit()
print(model.summary())

plt.scatter(X, y, alpha=0.6, label="Data")
plt.plot(X, model.predict(X_const), "r-", label="Fitted line")
plt.xlabel("X"); plt.ylabel("Y"); plt.legend()
plt.title("Simple Linear Regression")
plt.savefig("../data/08_regression.png")
plt.show()
