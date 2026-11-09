# Text Classification using SVM

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report

# Select Categories
categories = [
    'comp.graphics',
    'rec.sport.baseball',
    'sci.space'
]

# Load Training Dataset
train_data = fetch_20newsgroups(
    subset='train',
    categories=categories,
    remove=('headers', 'footers', 'quotes')
)

# Load Testing Dataset
test_data = fetch_20newsgroups(
    subset='test',
    categories=categories,
    remove=('headers', 'footers', 'quotes')
)

# Display Dataset Information
print("Number of Training Documents:", len(train_data.data))
print("Number of Testing Documents:", len(test_data.data))

# Create TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english')

# Convert Text into Numerical Features
X_train = vectorizer.fit_transform(train_data.data)
X_test = vectorizer.transform(test_data.data)

# Separate Target Labels
y_train = train_data.target
y_test = test_data.target

# Create SVM Classifier
model = LinearSVC()

# Train the Model
model.fit(X_train, y_train)

# Predict Test Data
y_pred = model.predict(X_test)

# Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nClassification Accuracy: {:.2f}%".format(
    accuracy * 100
))

# Display Classification Report
print("\nClassification Report:")

print(classification_report(
    y_test,
    y_pred,
    target_names=train_data.target_names
))

# Display Actual and Predicted Labels
print("\nActual Labels:")
print(y_test)

print("\nPredicted Labels:")
print(y_pred)

# Final Result
print("\nText Classification using SVM completed successfully.")