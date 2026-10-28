"""
Topic 18: Logistic Regression
"""
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=300, n_features=2, n_informative=2,
                           n_redundant=0, random_state=42)
model = LogisticRegression().fit(X, y)
print("Coefficients:", model.coef_)
print("Intercept   :", model.intercept_)

y_pred = model.predict(X)
print("\nConfusion Matrix:\n", confusion_matrix(y, y_pred))
print("\nClassification Report:\n", classification_report(y, y_pred))
