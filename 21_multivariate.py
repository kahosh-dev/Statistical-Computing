"""
Topic 21: Multivariate Statistical Analysis (Clustering example)
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.7, random_state=42)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10).fit(X)

plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap="viridis", alpha=0.7)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],
            c="red", s=200, marker="X", label="Centroids")
plt.title("K-Means Clustering")
plt.legend()
plt.savefig("../data/21_kmeans.png")
plt.show()
print("Cluster sizes:", np.bincount(kmeans.labels_))
