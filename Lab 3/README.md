# Lab 3 - List Operations for House Data

## Problem Statement

This lab focuses on working with lists in Python to store and display multiple house sizes. The goal is to understand how to create a list data structure, populate it with multiple values, and iterate through the list to display each element individually. This builds on the basic Python concepts from Lab 1 and prepares for more complex data handling in machine learning.

## Implementation Approach

The implementation is a straightforward Python program that demonstrates list creation and iteration.

### Creating the List

The program starts by creating a list called house_sizes that contains six different house sizes in square feet. The list includes values like 1200, 1500, 2000, 1800, 2500, and 1650. This represents a small dataset of houses with different sizes.

### Displaying the Data

The program first prints a header message to make the output more readable. It then uses a for loop to iterate through each element in the list. For each house size, it prints a formatted message showing the size in square feet. This demonstrates how loops can process multiple items sequentially without writing separate print statements for each one.

### Counting Elements

After displaying all the house sizes, the program uses the len() function to count how many houses are in the list and displays this total. This shows how to get the size of a list, which is useful for understanding the dataset dimensions.

## Running the Program

To run the program, execute:

```bash
python question3_house_sizes.py
```

The output will display each house size on a separate line followed by the total count of houses.

## Key Takeaways

This lab reinforces the importance of lists as a fundamental data structure in Python. Lists allow us to store multiple related values in a single variable, which is essential for working with datasets in machine learning. The for loop is a powerful tool for processing each item in a list without repetitive code. Understanding these basic operations is crucial before moving on to more complex data manipulation tasks.
