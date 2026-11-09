import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the Diabetes dataset
diabetes = load_diabetes()

X = diabetes.data
y = diabetes.target

print("Dataset Loaded Successfully")
print("Number of Samples:", X.shape[0])
print("Number of Features:", X.shape[1])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression using BMI only
X_train_bmi = X_train[:, 2].reshape(-1, 1)
X_test_bmi = X_test[:, 2].reshape(-1, 1)



--------------------------------------------------------------------------------------
linear_model = LinearRegression()

linear_model.fit(X_train_bmi, y_train)

y_pred_linear = linear_model.predict(X_test_bmi)

mse_linear = mean_squared_error(y_test, y_pred_linear)

r2_linear = r2_score(y_test, y_pred_linear)

print("\nLinear Regression (BMI Only)")
print("Mean Squared Error:", mse_linear)
print("R2 Score:", r2_linear)

------------------------------------------------------------------------------------------

multiple_model = LinearRegression()

multiple_model.fit(X_train, y_train)

y_pred_multiple = multiple_model.predict(X_test)

mse_multiple = mean_squared_error(y_test, y_pred_multiple)

r2_multiple = r2_score(y_test, y_pred_multiple)

print("\nMultiple Linear Regression (All Features)")
print("Mean Squared Error:", mse_multiple)
print("R2 Score:", r2_multiple)

--------------------------------------------------------------------------------------------
# Compare both models
print("\nModel Comparison")
print("Linear Regression MSE:", mse_linear)
print("Multiple Linear Regression MSE:", mse_multiple)

print("Linear Regression R2 Score:", r2_linear)
print("Multiple Linear Regression R2 Score:", r2_multiple)

# Plot Linear Regression results
sorted_indices = X_test_bmi[:, 0].argsort()

plt.scatter(X_test_bmi, y_test, label="Actual Data")
plt.plot(
    X_test_bmi[sorted_indices],
    y_pred_linear[sorted_indices],
    color='red',
    label="Regression Line"
)

plt.xlabel("BMI")
plt.ylabel("Disease Progression")
plt.title("Linear Regression using BMI")
plt.legend()
plt.show()

print("\nRegression Analysis Completed Successfully")