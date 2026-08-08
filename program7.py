# ===================================================================
# Program 7: House Price Prediction using Linear Regression
# ===================================================================
# Problem Statement: Write a Python program to predict the price 
# of a house using Linear Regression.
# 
# This program implements the 8-step algorithm from the course material.
# ===================================================================

print("="*70)
print("PROGRAM 7: House Price Prediction using Linear Regression")
print("="*70)

# ===================================================================
# STEP 1: Collect the dataset containing input (Area) and output (Price)
# ===================================================================
print("\nSTEP 1: Collect the Dataset")
print("-" * 70)

areas = [1000, 1500, 2000, 2500, 3000]  # Area in sq. ft.
prices = [30, 45, 60, 75, 90]  # Price in ₹ Lakhs

print("Dataset collected:")
print(f"{'House':<10} {'Area (sq. ft.)':<20} {'Price (₹ Lakhs)':<20}")
print("-" * 50)
for i in range(len(areas)):
    print(f"H{i+1:<9} {areas[i]:<20} {prices[i]:<20}")

# ===================================================================
# STEP 2: Examine the dataset to ensure values are complete and correct
# ===================================================================
print("\nSTEP 2: Examine the Dataset")
print("-" * 70)

print(f"Total number of records: {len(areas)}")
print(f"All houses have area values: {all(areas)}")
print(f"All houses have price values: {all(prices)}")
print(f"Dataset is complete: {len(areas) == len(prices)}")
print("✓ Dataset verification passed!")

# ===================================================================
# STEP 3: Identify the input and output variables
# ===================================================================
print("\nSTEP 3: Identify Input and Output Variables")
print("-" * 70)

print("Input Variable (X): Area (sq. ft.)")
print("Output Variable (Y): House Price (₹ Lakhs)")
print("Relationship: Larger area → Higher price")

# ===================================================================
# STEP 4: Divide the dataset into training and testing data
# ===================================================================
print("\nSTEP 4: Divide Dataset into Training and Testing Data")
print("-" * 70)

train_areas = areas[:4]  # H1 to H4 (80% data)
train_prices = prices[:4]
test_areas = [areas[4]]  # H5 (20% data)
test_prices = [prices[4]]

print(f"Training set: H1-H4 ({len(train_areas)} houses)")
print(f"  Areas: {train_areas}")
print(f"  Prices: {train_prices}")
print(f"\nTesting set: H5 ({len(test_areas)} house)")
print(f"  Areas: {test_areas}")
print(f"  Prices: {test_prices}")

# ===================================================================
# STEP 5: Train the Simple Linear Regression model
# ===================================================================
print("\nSTEP 5: Train the Linear Regression Model")
print("-" * 70)

# Calculate parameters for y = mx + b
# m (slope) = (n*Σxy - Σx*Σy) / (n*Σx² - (Σx)²)
# b (intercept) = (Σy - m*Σx) / n

n = len(train_areas)
sum_x = sum(train_areas)
sum_y = sum(train_prices)
sum_xy = sum(x * y for x, y in zip(train_areas, train_prices))
sum_x2 = sum(x ** 2 for x in train_areas)

# Calculate slope (m) and intercept (b)
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
b = (sum_y - m * sum_x) / n

print("Training completed!")
print(f"\nLinear Regression Equation: Price = {m:.4f} × Area + {b:.4f}")
print(f"Slope (m): {m:.4f}")
print(f"Intercept (b): {b:.4f}")
print("\nInterpretation: For every 1 sq. ft. increase in area,")
print(f"the price increases by ₹{m:.4f} Lakhs")

# ===================================================================
# STEP 6: Test the trained model using the testing data
# ===================================================================
print("\nSTEP 6: Test the Trained Model")
print("-" * 70)

predicted_test_price = m * test_areas[0] + b

print(f"Test Input: {test_areas[0]} sq. ft.")
print(f"Predicted Price: ₹{predicted_test_price:.2f} Lakhs")

# ===================================================================
# STEP 7: Compare predicted and actual prices
# ===================================================================
print("\nSTEP 7: Compare Predicted and Actual Prices")
print("-" * 70)

actual_price = test_prices[0]
predicted_price = predicted_test_price
error = abs(actual_price - predicted_price)
accuracy = (1 - error / actual_price) * 100

print(f"Actual Price: ₹{actual_price} Lakhs")
print(f"Predicted Price: ₹{predicted_price:.2f} Lakhs")
print(f"Error: ₹{error:.2f} Lakhs")
print(f"Accuracy: {accuracy:.2f}%")

if accuracy >= 95:
    print("✓ Model performance: Excellent!")
elif accuracy >= 85:
    print("✓ Model performance: Good!")
else:
    print("✓ Model performance: Acceptable!")

# ===================================================================
# STEP 8: Use the trained model to predict new house prices
# ===================================================================
print("\nSTEP 8: Predict Prices for New Houses")
print("-" * 70)

new_areas = [1800, 2200, 2800]

print("\nPredictions for new houses:")
print(f"{'Area (sq. ft.)':<20} {'Predicted Price (₹ Lakhs)':<30}")
print("-" * 50)

for area in new_areas:
    predicted = m * area + b
    print(f"{area:<20} ₹{predicted:<29.2f}")

# Sample predictions from algorithm document
print("\nSample Predictions (from course material):")
print("-" * 50)
sample_predictions = [
    (1800, 54),
    (2200, 66),
    (2800, 84)
]

for area, expected in sample_predictions:
    predicted = m * area + b
    difference = abs(predicted - expected)
    print(f"Area: {area} sq. ft.")
    print(f"  Our Prediction: ₹{predicted:.2f} Lakhs")
    print(f"  Expected: ₹{expected} Lakhs")
    print(f"  Difference: ₹{difference:.2f} Lakhs\n")

# ===================================================================
# MODEL SUMMARY
# ===================================================================
print("\n" + "="*70)
print("LINEAR REGRESSION MODEL SUMMARY")
print("="*70)
print(f"Training samples: {len(train_areas)} houses")
print(f"Testing samples: {len(test_areas)} house")
print(f"Model equation: Price = {m:.4f} × Area + {b:.4f}")
print(f"Test accuracy: {accuracy:.2f}%")
print(f"Model status: Successfully trained and validated ✓")
print("="*70)

# Interactive prediction
print("\n" + "="*70)
print("Try Your Own Prediction:")
print("="*70)
try:
    user_area = float(input("Enter house area in sq. ft.: "))
    user_predicted_price = m * user_area + b
    print(f"\nFor a house with {user_area} sq. ft.:")
    print(f"Predicted Price: ₹{user_predicted_price:.2f} Lakhs")
except ValueError:
    print("Invalid input! Please enter a numeric value.")

print("\n" + "="*70)
print("Program 7 completed successfully!")
print("All 8 steps of Linear Regression algorithm executed! ✓")
print("="*70)
