"""
Topic 10: Eigenvalues, Eigenvectors and PCA
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

X = load_iris().data
pca = PCA()
X_pca = pca.fit_transform(X)

print("Explained variance ratio:", pca.explained_variance_ratio_.round(3))
print("Eigenvalues:", pca.explained_variance_.round(3))

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(range(1,5), np.cumsum(pca.explained_variance_ratio_), "o-")
plt.xlabel("Components"); plt.ylabel("Cumulative explained variance")
plt.title("Scree / Cumulative Variance")
plt.subplot(1,2,2)
plt.scatter(X_pca[:,0], X_pca[:,1], c=load_iris().target, cmap="viridis")
plt.xlabel("PC1"); plt.ylabel("PC2"); plt.title("PCA Score Plot")
plt.tight_layout()
plt.savefig("../data/10_pca.png")
plt.show()
