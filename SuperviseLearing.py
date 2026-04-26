import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Load CSV using Pandas
df = pd.read_csv("house_prices.csv")
print("Original Data:")
print(df)

# Step 2: Clean data using Pandas
df=df.dropna()
df=df.drop_duplicates()
print("cleaned Data")
print(df)

# Step 3: Prepare input X and output y
X = df[["size_sqft"]]   # input / feature
Y = df["price"]         # output / target

print(X)
print(Y)

# Step 4: Train-test split
# 80% data for training, 20% data for testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Input:")
print(X_train)

print("\nTesting Input:")
print(X_test)

# Step 5: Create Linear Regression model
model = LinearRegression()
# Step 6: Train model
model.fit(X_train, y_train)
print("\nModel trained successfully")


# Step 7: Predict using test data
y_pred = model.predict(X_test)

print("\nActual Prices:")
print(y_test.values)

print("\nPredicted Prices:")
print(y_pred)

# Step 8: Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Squared Error:", mse)
print("R2 Score:", r2)


# Step 9: Predict new house price
new_house = np.array([[2400]])
predicted_price = model.predict(new_house)

print("\nPredicted price for 2400 sqft house:")
print(predicted_price[0])


# Step 10: Visualize using Matplotlib
plt.scatter(X, Y, label="Actual Data")
plt.plot(X, model.predict(X), label="Regression Line")

plt.xlabel("House Size in Sqft")
plt.ylabel("House Price")
plt.title("House Price Prediction using Linear Regression")
plt.legend()
plt.show()
