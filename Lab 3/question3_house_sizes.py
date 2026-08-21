# Python program to store house sizes in a list and display each element

# Create a list of house sizes (in square feet)
house_sizes = [1200, 1500, 2000, 1800, 2500, 1650]

# Display a header message
print("House Sizes (in square feet):")
print("-" * 30)

# Loop through the list and display each house size
for size in house_sizes:
    print(f"House size: {size} sq ft")

# Display total number of houses
print("-" * 30)
print(f"Total houses: {len(house_sizes)}")
