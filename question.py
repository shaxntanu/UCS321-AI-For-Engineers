# ===================================================================
# AI For Engineers - Unit 1 Programs
# House Price Prediction using Linear Regression and Python Basics
# ===================================================================

# Program 1: Store house data and display values with data types
# ===================================================================
print("\n" + "="*70)
print("PROGRAM 1: Store and Display House Data with Data Types")
print("="*70)

# Store house information
house_size = 2000  # in sq. ft.
house_price = 60  # in Lakhs
city_name = "Mumbai"
is_available = True

# Display values
print(f"\nHouse Size: {house_size} sq. ft.")
print(f"House Price: ₹{house_price} Lakhs")
print(f"City Name: {city_name}")
print(f"Availability Status: {is_available}")

# Display data types
print(f"\nData type of house_size: {type(house_size)}")
print(f"Data type of house_price: {type(house_price)}")
print(f"Data type of city_name: {type(city_name)}")
print(f"Data type of is_available: {type(is_available)}")


# Program 2: Calculate operations on two house prices
# ===================================================================
print("\n" + "="*70)
print("PROGRAM 2: Calculate Operations on Two House Prices")
print("="*70)

price1 = 45  # in Lakhs
price2 = 30  # in Lakhs

total_cost = price1 + price2
difference = price1 - price2
multiplication = price1 * price2
division = price1 / price2

print(f"\nHouse 1 Price: ₹{price1} Lakhs")
print(f"House 2 Price: ₹{price2} Lakhs")
print(f"\nTotal Cost: ₹{total_cost} Lakhs")
print(f"Difference: ₹{difference} Lakhs")
print(f"Multiplication: {multiplication}")
print(f"Division: {division:.2f}")


# Program 3: Store house sizes in a list and display each element
# ===================================================================
print("\n" + "="*70)
print("PROGRAM 3: Store and Display House Sizes from List")
print("="*70)

house_sizes = [1000, 1500, 2000, 2500, 3000]

print("\nHouse sizes in the list:")
for i, size in enumerate(house_sizes, 1):
    print(f"House {i}: {size} sq. ft.")


# Program 4: Function to estimate house price based on size
# ===================================================================
print("\n" + "="*70)
print("PROGRAM 4: Function to Estimate House Price Based on Size")
print("="*70)

def estimate_house_price(size):
    """
    Estimate house price based on size using a simple formula.
    Formula: Price (in Lakhs) = Size / 33.33
    This approximates the linear relationship from the dataset.
    """
    price = size / 33.33
    return round(price, 2)

# Test the function
test_sizes = [1000, 1800, 2200, 2500, 3000]

print("\nEstimated prices:")
for size in test_sizes:
    estimated_price = estimate_house_price(size)
    print(f"Size: {size} sq. ft. → Estimated Price: ₹{estimated_price} Lakhs")


# Program 5: Classify house as Affordable or Expensive
# ===================================================================
print("\n" + "="*70)
print("PROGRAM 5: Classify House as Affordable or Expensive")
print("="*70)

def classify_house(price):
    """
    Classify a house based on its price.
    Affordable: price <= 50 Lakhs
    Expensive: price > 50 Lakhs
    """
    if price <= 50:
        return "Affordable"
    else:
        return "Expensive"

# Test the classification
test_prices = [30, 45, 60, 75, 90]

print("\nHouse Classification:")
for price in test_prices:
    classification = classify_house(price)
    print(f"Price: ₹{price} Lakhs → Classification: {classification}")


# Program 6: Display all house sizes stored in a list
# ===================================================================
print("\n" + "="*70)
print("PROGRAM 6: Display All House Sizes from List")
print("="*70)

house_sizes_list = [1000, 1500, 2000, 2500, 3000]

print("\nAll house sizes:")
print(house_sizes_list)

print("\nDetailed view:")
for index, size in enumerate(house_sizes_list):
    print(f"Index {index}: {size} sq. ft.")


# Program 7: Predict house price using Linear Regression
# ===================================================================
print("\n" + "="*70)
print("PROGRAM 7: House Price Prediction using Linear Regression")
print("="*70)

# Step 1: Collect the dataset
areas = [1000, 1500, 2000, 2500, 3000]  # Area in sq. ft.
prices = [30, 45, 60, 75, 90]  # Price in Lakhs

print("\nStep 1: Dataset collected")
print("Areas (sq. ft.):", areas)
print("Prices (₹ Lakhs):", prices)

# Step 2: Examine the dataset
print("\nStep 2: Dataset examination")
print(f"Number of data points: {len(areas)}")
print("Dataset is complete: All houses have both area and price values")

# Step 3: Identify input and output variables
print("\nStep 3: Variables identified")
print("Input (X): Area (sq. ft.)")
print("Output (Y): House Price (₹ Lakhs)")

# Step 4: Divide dataset into training and testing data
train_areas = areas[:4]  # H1 to H4
train_prices = prices[:4]
test_areas = [areas[4]]  # H5
test_prices = [prices[4]]

print("\nStep 4: Dataset divided")
print(f"Training data: {len(train_areas)} houses (H1-H4)")
print(f"Testing data: {len(test_areas)} house (H5)")

# Step 5: Train the Linear Regression model
# Calculate slope (m) and intercept (b) for y = mx + b
n = len(train_areas)
sum_x = sum(train_areas)
sum_y = sum(train_prices)
sum_xy = sum(x * y for x, y in zip(train_areas, train_prices))
sum_x2 = sum(x ** 2 for x in train_areas)

# Calculate slope (m) and intercept (b)
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
b = (sum_y - m * sum_x) / n

print("\nStep 5: Model trained")
print(f"Linear Regression equation: Price = {m:.4f} × Area + {b:.4f}")
print(f"Slope (m): {m:.4f}")
print(f"Intercept (b): {b:.4f}")

# Step 6: Test the trained model
print("\nStep 6: Testing the model")
predicted_test_price = m * test_areas[0] + b
print(f"Test input: {test_areas[0]} sq. ft.")
print(f"Predicted price: ₹{predicted_test_price:.2f} Lakhs")

# Step 7: Compare predicted and actual prices
print("\nStep 7: Comparison")
print(f"Actual price: ₹{test_prices[0]} Lakhs")
print(f"Predicted price: ₹{predicted_test_price:.2f} Lakhs")
error = abs(test_prices[0] - predicted_test_price)
accuracy = (1 - error / test_prices[0]) * 100
print(f"Error: ₹{error:.2f} Lakhs")
print(f"Accuracy: {accuracy:.2f}%")

# Step 8: Use the model to predict new house prices
print("\nStep 8: Predicting new house prices")
new_areas = [1800, 2200, 2800]

print("\nPredictions for new houses:")
print("-" * 40)
for area in new_areas:
    predicted_price = m * area + b
    print(f"Area: {area} sq. ft. → Predicted Price: ₹{predicted_price:.2f} Lakhs")

# Additional predictions from the algorithm document
print("\nSample Predictions (as per algorithm):")
print("-" * 40)
sample_predictions = [
    (1800, 54),
    (2200, 66),
    (2800, 84)
]
for area, expected in sample_predictions:
    predicted = m * area + b
    print(f"Area: {area} sq. ft. → Predicted: ₹{predicted:.2f} Lakhs (Expected: ₹{expected} Lakhs)")

# Summary
print("\n" + "="*70)
print("LINEAR REGRESSION MODEL SUMMARY")
print("="*70)
print(f"Training samples: {len(train_areas)}")
print(f"Test samples: {len(test_areas)}")
print(f"Model equation: Price = {m:.4f} × Area + {b:.4f}")
print(f"Model accuracy on test data: {accuracy:.2f}%")
print("="*70)

print("\n✓ All 7 programs completed successfully!")
print("="*70)
