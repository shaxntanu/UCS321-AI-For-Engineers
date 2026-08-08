# ===================================================================
# Program 4: Function to Estimate House Price Based on Size
# ===================================================================
# Problem Statement: Write a Python function to estimate the price 
# of a house based on its size.
# ===================================================================

print("="*70)
print("PROGRAM 4: Function to Estimate House Price Based on Size")
print("="*70)

def estimate_house_price(size):
    """
    Estimate house price based on size using a simple formula.
    Formula: Price (in Lakhs) = Size / 33.33
    This approximates the linear relationship from the dataset
    where 1000 sq.ft. ≈ ₹30 Lakhs.
    
    Parameters:
        size (int/float): House size in square feet
    
    Returns:
        float: Estimated price in Lakhs
    """
    price = size / 33.33
    return round(price, 2)


# Test the function with various house sizes
test_sizes = [1000, 1500, 1800, 2000, 2200, 2500, 2800, 3000]

print("\nEstimating house prices:")
print("-" * 50)
print(f"{'Size (sq. ft.)':<20} {'Estimated Price (₹ Lakhs)':<30}")
print("-" * 50)

for size in test_sizes:
    estimated_price = estimate_house_price(size)
    print(f"{size:<20} ₹{estimated_price:<29.2f}")

# Interactive input (optional)
print("\n" + "="*70)
print("Try with your own input:")
try:
    user_size = float(input("Enter house size in sq. ft.: "))
    user_price = estimate_house_price(user_size)
    print(f"Estimated price for {user_size} sq. ft.: ₹{user_price} Lakhs")
except ValueError:
    print("Invalid input! Please enter a numeric value.")

print("\n" + "="*70)
print("Program 4 completed successfully!")
print("="*70)
