# ===================================================================
# Program 5: Classify House as Affordable or Expensive
# ===================================================================
# Problem Statement: Write a Python program to classify a house as 
# "Affordable" or "Expensive" based on its price.
# ===================================================================

print("="*70)
print("PROGRAM 5: Classify House as Affordable or Expensive")
print("="*70)

def classify_house(price):
    """
    Classify a house based on its price.
    
    Classification criteria:
    - Affordable: price <= 50 Lakhs
    - Expensive: price > 50 Lakhs
    
    Parameters:
        price (int/float): House price in Lakhs
    
    Returns:
        str: Classification result
    """
    if price <= 50:
        return "Affordable"
    else:
        return "Expensive"


# Test the classification with sample prices
test_prices = [30, 40, 45, 50, 55, 60, 75, 90]

print("\nHouse Price Classification:")
print("-" * 50)
print(f"{'Price (₹ Lakhs)':<20} {'Classification':<30}")
print("-" * 50)

for price in test_prices:
    classification = classify_house(price)
    print(f"₹{price:<19} {classification:<30}")

# Enhanced classification with multiple categories
print("\n" + "="*70)
print("BONUS: Enhanced Classification with Multiple Categories")
print("="*70)

def classify_house_enhanced(price):
    """
    Enhanced classification with multiple categories.
    
    Classification criteria:
    - Budget: price <= 30 Lakhs
    - Affordable: 30 < price <= 50 Lakhs
    - Mid-range: 50 < price <= 70 Lakhs
    - Expensive: 70 < price <= 90 Lakhs
    - Luxury: price > 90 Lakhs
    """
    if price <= 30:
        return "Budget"
    elif price <= 50:
        return "Affordable"
    elif price <= 70:
        return "Mid-range"
    elif price <= 90:
        return "Expensive"
    else:
        return "Luxury"


print("\nEnhanced Classification:")
print("-" * 50)
for price in test_prices:
    classification = classify_house_enhanced(price)
    print(f"₹{price} Lakhs → {classification}")

# Interactive input
print("\n" + "="*70)
print("Try with your own input:")
try:
    user_price = float(input("Enter house price in Lakhs: "))
    user_classification = classify_house(user_price)
    user_classification_enhanced = classify_house_enhanced(user_price)
    print(f"\nSimple Classification: {user_classification}")
    print(f"Enhanced Classification: {user_classification_enhanced}")
except ValueError:
    print("Invalid input! Please enter a numeric value.")

print("\n" + "="*70)
print("Program 5 completed successfully!")
print("="*70)
