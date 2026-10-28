"""
Topic 9: Matrix Algebra in Statistics
"""
import numpy as np

A = np.array([[2, 1], [1, 3]], dtype=float)
B = np.array([[1, 0], [2, 1]], dtype=float)
b = np.array([5, 7], dtype=float)

print("A + B =\n", A + B)
print("\nA @ B =\n", A @ B)
print("\nA.T =\n", A.T)
print("\ndet(A) =", np.linalg.det(A))
print("\nA inverse =\n", np.linalg.inv(A))
print("\nSolution of Ax = b:", np.linalg.solve(A, b))
