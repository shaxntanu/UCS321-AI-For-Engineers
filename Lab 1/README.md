# Lab 1 - Python Basics for House Price Prediction

## Problem Statement

This lab introduces fundamental Python programming concepts through the context of house price prediction. The goal is to learn basic data types, operations, lists, functions, conditional logic, and linear regression implementation from scratch. The lab progresses from simple data storage to building a complete machine learning model without using any external libraries.

## Implementation Approach

The lab is divided into seven programs, each building upon the previous one to gradually introduce Python concepts.

### Program 1: Data Types and Storage

The first program demonstrates how to store house information using different Python data types. It stores house size as an integer, price as an integer, city name as a string, and availability status as a boolean. The program displays both the values and their data types using the type() function. This establishes the foundation for understanding how Python handles different kinds of data.

### Program 2: Basic Operations

The second program performs arithmetic operations on house prices. It calculates the average price of two houses, finds the difference between prices, and determines the total value. This introduces basic mathematical operators and shows how to manipulate numerical data in Python.

### Program 3: Lists

The third program introduces lists by storing multiple house sizes in a single data structure. It demonstrates how to create a list, access individual elements using indexing, and find the length of the list. This is essential for handling datasets in machine learning.

### Program 4: Functions

The fourth program encapsulates price estimation logic in a reusable function. The function takes house size as input and returns an estimated price based on a simple formula. This teaches function definition, parameters, return values, and code reusability.

### Program 5: Conditional Logic

The fifth program uses if-else statements to classify houses based on their price. It categorizes houses as affordable, mid-range, or luxury depending on their price value. This introduces conditional statements and comparison operators.

### Program 6: Loops

The sixth program demonstrates iteration by looping through a list of house sizes and displaying each one. It uses a for loop to process multiple items sequentially, which is a fundamental pattern for working with datasets.

### Program 7: Linear Regression from Scratch

The final program brings everything together to implement linear regression without using any machine learning libraries. It follows the complete machine learning pipeline:

1. **Data Collection**: Stores house areas and corresponding prices
2. **Data Examination**: Checks the dataset size and completeness
3. **Variable Identification**: Defines input (area) and output (price)
4. **Train-Test Split**: Divides data into training (4 houses) and testing (1 house) sets
5. **Model Training**: Calculates slope (m) and intercept (b) using the least squares method
6. **Testing**: Predicts price for the test house and compares with actual price
7. **Error Calculation**: Computes the difference between predicted and actual values
8. **New Predictions**: Uses the trained model to predict prices for new houses

The linear regression equation is calculated manually using the formulas:
- Slope (m) = (n * sum(xy) - sum(x) * sum(y)) / (n * sum(x^2) - sum(x)^2)
- Intercept (b) = (sum(y) - m * sum(x)) / n

## Running the Programs

Each program can be run independently:

```bash
python 01_house_data_and_datatypes.py
python 02_house_price_operations.py
python 03_house_sizes_list.py
python 04_estimate_price_function.py
python 05_classify_house_price.py
python 06_display_house_sizes.py
python 07_linear_regression_prediction.py
```

## Key Takeaways

This lab builds a complete understanding of Python programming fundamentals while staying within the context of a real-world problem. By implementing linear regression from scratch, it demystifies the mathematical foundations of machine learning and shows that complex models are built from simple programming concepts. The progression from basic data types to a working machine learning model provides a solid foundation for more advanced AI topics.
