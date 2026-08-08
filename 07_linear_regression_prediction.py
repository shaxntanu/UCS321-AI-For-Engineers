# Program 7: House Price Prediction using Linear Regression

print ("HOUSE PRICE PREDICTION USING LINEAR REGRESSION")
print ()

# Step 1: Collect the dataset
areas = [1000, 1500, 2000, 2500, 3000]  # Area in sq. ft.
prices = [30, 45, 60, 75, 90]  # Price in Lakhs

print ("Step 1: Dataset collected")
print ("Areas:", areas)
print ("Prices:", prices)
print ()

# Step 2: Examine the dataset
print ("Step 2: Dataset examined")
print ("Number of houses:", len(areas))
print ("All houses have area and price values")
print ()

# Step 3: Identify input and output
print ("Step 3: Variables identified")
print ("Input: Area (sq. ft.)")
print ("Output: House Price (Lakhs)")
print ()

# Step 4: Divide into training and testing data
train_areas = [areas[0], areas[1], areas[2], areas[3]]  # H1 to H4
train_prices = [prices[0], prices[1], prices[2], prices[3]]
test_area = areas[4]  # H5
test_price = prices[4]

print ("Step 4: Dataset divided")
print ("Training data: 4 houses (H1-H4)")
print ("Testing data: 1 house (H5)")
print ()

# Step 5: Train the Linear Regression model
# Calculate slope (m) and intercept (b) for: Price = m * Area + b

n = 4  # number of training houses
sum_x = train_areas[0] + train_areas[1] + train_areas[2] + train_areas[3]
sum_y = train_prices[0] + train_prices[1] + train_prices[2] + train_prices[3]
sum_xy = (train_areas[0]*train_prices[0]) + (train_areas[1]*train_prices[1]) + (train_areas[2]*train_prices[2]) + (train_areas[3]*train_prices[3])
sum_x2 = (train_areas[0]*train_areas[0]) + (train_areas[1]*train_areas[1]) + (train_areas[2]*train_areas[2]) + (train_areas[3]*train_areas[3])

m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
b = (sum_y - m * sum_x) / n

print ("Step 5: Model trained")
print ("Slope (m):", m)
print ("Intercept (b):", b)
print ("Equation: Price =", m, "* Area +", b)
print ()

# Step 6: Test the model
predicted_price = m * test_area + b

print ("Step 6: Testing the model")
print ("Test input:", test_area, "sq. ft.")
print ("Predicted price:", predicted_price, "Lakhs")
print ()

# Step 7: Compare predicted and actual
print ("Step 7: Comparison")
print ("Actual price:", test_price, "Lakhs")
print ("Predicted price:", predicted_price, "Lakhs")
error = test_price - predicted_price
if error < 0:
    error = -error  # make positive
print ("Error:", error, "Lakhs")
print ()

# Step 8: Predict new house prices
print ("Step 8: Predict new house prices")

new_area1 = 1800
new_price1 = m * new_area1 + b
print ("Area:", new_area1, "sq. ft. → Predicted Price:", new_price1, "Lakhs")

new_area2 = 2200
new_price2 = m * new_area2 + b
print ("Area:", new_area2, "sq. ft. → Predicted Price:", new_price2, "Lakhs")

new_area3 = 2800
new_price3 = m * new_area3 + b
print ("Area:", new_area3, "sq. ft. → Predicted Price:", new_price3, "Lakhs")

print ()
print ("Linear Regression completed successfully!")
