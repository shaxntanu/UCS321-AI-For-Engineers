# ===================================================================
# Program 2: Calculate Operations on Two House Prices
# ===================================================================
# Problem Statement: Write a Python program to calculate the total 
# cost, difference, multiplication, and division of two house prices.
# ===================================================================

print("="*70)
print("PROGRAM 2: Calculate Operations on Two House Prices")
print("="*70)

# Store two house prices
price1 = 45  # in Lakhs
price2 = 30  # in Lakhs

# Perform calculations
total_cost = price1 + price2
difference = price1 - price2
multiplication = price1 * price2
division = price1 / price2

# Display results
print(f"\nHouse 1 Price: ₹{price1} Lakhs")
print(f"House 2 Price: ₹{price2} Lakhs")
print(f"\nTotal Cost (Addition): ₹{total_cost} Lakhs")
print(f"Difference (Subtraction): ₹{difference} Lakhs")
print(f"Multiplication: {multiplication}")
print(f"Division: {division:.2f}")

print("\n" + "="*70)
print("Program 2 completed successfully!")
print("="*70)
