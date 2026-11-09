# Decision Tree Classification using Iris Dataset

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Step 1: Load Iris Dataset
iris = load_iris()

X = iris.data
y = iris.target

# Step 2: Display Dataset Information
print("Number of Samples:", X.shape[0])
print("Number of Features:", X.shape[1])

print("\nFeature Names:")
print(iris.feature_names)

print("\nClass Names:")
print(iris.target_names)


# Step 3: Split Dataset (80:20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))


# Step 4: Create Decision Tree Model
model = DecisionTreeClassifier(
    criterion='gini',
    random_state=42
)

# Step 5: Train the Model
model.fit(X_train, y_train)

# Step 6: Make Predictions
y_pred = model.predict(X_test)

# Step 7: Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n--- Decision Tree Results (80:20) ---")
print("Actual Classes:")
print(y_test)

print("\nPredicted Classes:")
print(y_pred)

print("\nAccuracy: {:.2f}%".format(accuracy * 100))

# Step 8: Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Step 9: Classification Report
print("\nClassification Report:")
print(classification_report(
    y_test, y_pred, target_names=iris.target_names
))


# Step 10: Visualize Decision Tree
plt.figure(figsize=(15, 8))

plot_tree(
    model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True
)

plt.title("Decision Tree Classification - Iris Dataset")
plt.show()


# Step 11: Try 70:30 Train-Test Split
X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model2 = DecisionTreeClassifier(
    criterion='gini',
    random_state=42
)

model2.fit(X_train2, y_train2)

y_pred2 = model2.predict(X_test2)

accuracy2 = accuracy_score(y_test2, y_pred2)

print("\n--- Decision Tree Results (70:30) ---")

print("Training Samples:", len(X_train2))
print("Testing Samples:", len(X_test2))

print("\nAccuracy: {:.2f}%".format(accuracy2 * 100))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test2, y_pred2))

print("\nClassification Report:")
print(classification_report(
    y_test2, y_pred2, target_names=iris.target_names
))


# Step 12: Model Comparison
print("\n--- Model Comparison ---")

print("Accuracy (80:20): {:.2f}%".format(accuracy * 100))
print("Accuracy (70:30): {:.2f}%".format(accuracy2 * 100))