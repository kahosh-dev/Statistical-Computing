"""
Topic 14: Statistical Data Visualization
"""
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = [iris.target_names[i] for i in iris.target]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
sns.histplot(data=df, x="sepal length (cm)", hue="species", ax=axes[0,0])
sns.boxplot(data=df, x="species", y="petal length (cm)", ax=axes[0,1])
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species", ax=axes[1,0])
sns.kdeplot(data=df, x="sepal width (cm)", hue="species", fill=True, ax=axes[1,1])
plt.tight_layout()
plt.savefig("../data/14_viz.png")
plt.show()
