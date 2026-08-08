# ===================================================================
# Program 1: Store and Display House Data with Data Types
# ===================================================================
# Problem Statement: Write a Python program to store the size of a 
# house, its price, city name, and availability status, and display 
# their values and data types.
# ===================================================================

print("="*70)
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

print("\n" + "="*70)
print("Program 1 completed successfully!")
print("="*70)
