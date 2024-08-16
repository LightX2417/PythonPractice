import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import joblib

# Load the dataset
data = pd.read_csv("housing.csv")

# Display basic information about the dataset
print(data.info())

# Separate numeric and categorical features
numeric_features = data.select_dtypes(include=[np.number]).columns.tolist()
categorical_features = data.select_dtypes(include=[object]).columns.tolist()

# Check if 'median_house_value' is in the categorical features and remove it
if "median_house_value" in categorical_features:
    categorical_features.remove("median_house_value")

# Drop rows with missing target values (median_house_value)
data = data.dropna(subset=["median_house_value"])

# Handle missing values for numeric features
numeric_imputer = SimpleImputer(strategy="median")
data[numeric_features] = numeric_imputer.fit_transform(data[numeric_features])

# Handle missing values for categorical features
categorical_imputer = SimpleImputer(strategy="most_frequent")
data[categorical_features] = categorical_imputer.fit_transform(
    data[categorical_features]
)

# Select features and target variable
X = data[
    [
        "longitude",
        "latitude",
        "housing_median_age",
        "total_rooms",
        "total_bedrooms",
        "population",
        "households",
        "median_income",
        "ocean_proximity",
    ]
]
y = data["median_house_value"]

# One-hot encode the 'ocean_proximity' feature
X = pd.get_dummies(X, columns=["ocean_proximity"], drop_first=True)

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Cross-validation
cv_scores = cross_val_score(model, X_scaled, y, cv=5, scoring="neg_mean_squared_error")
print(f"Cross-Validated MSE: {-np.mean(cv_scores)}")

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Plotting the actual vs. predicted prices
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs. Predicted Prices")
plt.show()

# Plotting the residuals (errors)
residuals = y_test - y_pred
plt.figure(figsize=(10, 6))
sns.histplot(residuals, kde=True)
plt.xlabel("Residuals")
plt.title("Residuals Distribution")
plt.show()

# Save the model and scaler
joblib.dump(model, "house_price_model.pkl")
joblib.dump(scaler, "scaler.pkl")
