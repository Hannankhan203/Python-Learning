import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

wine = load_wine()
X = wine.data
y = wine.target

print("Dataset loaded successfully!")
print(f"Number of wine samples: {X.shape[0]}")
print(f"Number of features: {X.shape[1]}")
print(f"Wine types: {np.unique(y)}")
print(f"Feature names: {wine.feature_names}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(f"\nTraining set size: {X_train.shape[0]} wines")
print(f"Testing set size: {X_test.shape[0]} wines")

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

print("\nKNN model trained with k=5")

y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model accuracy on test set: {accuracy:.2f} ({accuracy*100:.1f}%)")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
colors = ['red', 'green', 'blue']
for i, color in enumerate(colors):
    plt.scatter(X[y == i, 0], X[y == i, 1], c=color, label=f'Wine Class {i}', alpha=0.7)

plt.xlabel('Alcohol Content')
plt.ylabel('Malic Acid')
plt.title('Wine Classes: Alcohol vs Malic Acid')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
for i, color in enumerate(colors):
    plt.scatter(X[y == i, 0], X[y == i, 9], c=color, label=f'Wine Class {i}', alpha=0.7)

plt.xlabel('Alcohol Content')
plt.ylabel('Color Intensity')
plt.title('Wine Classes: Alcohol vs Color Intensity')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\nFirst 10 predictions vs actual:")
print("Predicted | Actual")
print("-" * 18)
for i in range(10):
    print(f"    {y_pred[i]}     |    {y_test[i]}")