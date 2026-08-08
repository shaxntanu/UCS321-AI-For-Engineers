# ===================================================================
# Program 3: Store and Display House Sizes from List
# ===================================================================
# Problem Statement: Write a Python program to store house sizes 
# in a list and display each element.
# ===================================================================

print("="*70)
print("PROGRAM 3: Store and Display House Sizes from List")
print("="*70)

# Store house sizes in a list
house_sizes = [1000, 1500, 2000, 2500, 3000]

# Display the entire list
print("\nHouse sizes list:", house_sizes)

# Display each element with index
print("\nDisplaying each element:")
print("-" * 40)
for i, size in enumerate(house_sizes, 1):
    print(f"House {i}: {size} sq. ft.")

# Alternative method using index
print("\nAlternative display using index:")
print("-" * 40)
for i in range(len(house_sizes)):
    print(f"Index {i}: {house_sizes[i]} sq. ft.")

print("\n" + "="*70)
print("Program 3 completed successfully!")
print("="*70)
