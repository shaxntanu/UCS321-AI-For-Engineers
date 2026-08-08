# ===================================================================
# Program 6: Display All House Sizes from List
# ===================================================================
# Problem Statement: Write a Python program to display all house 
# sizes stored in a list.
# ===================================================================

print("="*70)
print("PROGRAM 6: Display All House Sizes from List")
print("="*70)

# Store house sizes in a list
house_sizes_list = [1000, 1500, 2000, 2500, 3000]

# Method 1: Display the entire list
print("\nMethod 1: Display entire list")
print("-" * 40)
print("House sizes:", house_sizes_list)

# Method 2: Display with detailed view using index
print("\nMethod 2: Detailed view with index")
print("-" * 40)
for index, size in enumerate(house_sizes_list):
    print(f"Index {index}: {size} sq. ft.")

# Method 3: Display with house numbers
print("\nMethod 3: Display with house numbers")
print("-" * 40)
for i, size in enumerate(house_sizes_list, 1):
    print(f"House {i}: {size} sq. ft.")

# Method 4: Display using while loop
print("\nMethod 4: Display using while loop")
print("-" * 40)
i = 0
while i < len(house_sizes_list):
    print(f"Position {i+1}: {house_sizes_list[i]} sq. ft.")
    i += 1

# Additional list operations
print("\n" + "="*70)
print("Additional List Information:")
print("="*70)
print(f"Total number of houses: {len(house_sizes_list)}")
print(f"Smallest house size: {min(house_sizes_list)} sq. ft.")
print(f"Largest house size: {max(house_sizes_list)} sq. ft.")
print(f"Average house size: {sum(house_sizes_list) / len(house_sizes_list):.2f} sq. ft.")
print(f"Total area of all houses: {sum(house_sizes_list)} sq. ft.")

# Formatted table display
print("\nFormatted Table Display:")
print("-" * 40)
print(f"{'House No.':<15} {'Size (sq. ft.)':<25}")
print("-" * 40)
for i, size in enumerate(house_sizes_list, 1):
    print(f"House {i:<10} {size:<25}")

print("\n" + "="*70)
print("Program 6 completed successfully!")
print("="*70)
