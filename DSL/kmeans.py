# Import required libraries
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()

X = iris.data

print("Number of Samples:", X.shape[0])
print("Number of Features:", X.shape[1])

print("\nFeature Names:")
for feature in iris.feature_names:
    print(feature)

kmeans = KMeans(n_clusters=3,random_state=42,n_init=10)

kmeans.fit(X)

labels = kmeans.labels_

print("\nCluster Assignment of Each Sample:")
print(labels)

centers = kmeans.cluster_centers_

print("\nCluster Centers (Centroids):")
print(centers)

counts = np.bincount(labels)

print("\nNumber of Samples in Each Cluster:")

for i, count in enumerate(counts):
    print("Cluster", i, ":", count)

print("\nK-Means Inertia:")
print(kmeans.inertia_)

plt.figure(figsize=(8, 6))

plt.scatter(X[:, 2],X[:, 3],c=labels,s=50,alpha=0.7)

plt.scatter(centers[:, 2],centers[:, 3], marker='X',s=200,edgecolor='black',label='Cluster Centers')

plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("K-Means Clustering of Iris Dataset")
plt.legend()

plt.show()







from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

kmeans.fit(X)

y_pred = kmeans.predict(X)

print("Cluster Labels:", y_pred)

print("Centroids:\n", kmeans.cluster_centers_)

plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='rainbow')

plt.title("K-Means Clustering")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()