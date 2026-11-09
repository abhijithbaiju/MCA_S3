import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# Load Wine Dataset
wine = load_wine()

X = wine.data
y = wine.target

# Display Dataset Information
print("Number of Samples:", X.shape[0])
print("Number of Features:", X.shape[1])
print("Number of Classes:", len(wine.target_names))

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# Standardize Features
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# One-Hot Encoding
y_train = to_categorical(y_train, num_classes=3)
y_test_encoded = to_categorical(y_test, num_classes=3)

# Create Feedforward Neural Network
model = Sequential([
    Dense(16, activation='relu', input_shape=(13,)),
    Dense(8, activation='relu'),
    Dense(3, activation='softmax')
])

# Compile Model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train Model
history = model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=8,
    validation_split=0.2,
    verbose=1
)

# Evaluate Model
loss, accuracy = model.evaluate(
    X_test, y_test_encoded, verbose=0
)

print("\nTest Loss:", loss)
print("Test Accuracy: {:.2f}%".format(accuracy * 100))

# Make Predictions
y_pred_prob = model.predict(X_test, verbose=0)
y_pred = np.argmax(y_pred_prob, axis=1)

y_actual = np.argmax(y_test_encoded, axis=1)

# Calculate Accuracy
print("\nClassification Accuracy: {:.2f}%".format(
    accuracy_score(y_actual, y_pred) * 100
))

# Classification Report
print("\nClassification Report:")
print(classification_report(
    y_actual, y_pred, target_names=wine.target_names
))

# Confusion Matrix
cm = confusion_matrix(y_actual, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Plot Training and Validation Accuracy
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')

plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title("Training and Validation Accuracy")
plt.legend()
plt.grid(True)
plt.show()

# Plot Training and Validation Loss
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')

plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Training and Validation Loss")
plt.legend()
plt.grid(True)
plt.show()