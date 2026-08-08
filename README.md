# 🏠 AI For Engineers - Python Programming Lab

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Python programming lab exercises focused on house price prediction and data analysis. This repository contains hands-on programs that demonstrate fundamental programming concepts using real-world house pricing scenarios.

## 📚 Table of Contents

- [Overview](#overview)
- [Lab 1 - Python Basics & Linear Regression](#lab-1---python-basics--linear-regression)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Learning Outcomes](#learning-outcomes)
- [Contributing](#contributing)

## 🎯 Overview

This repository contains practical Python programs designed for learning AI and machine learning concepts through house price prediction examples. Each program builds upon previous concepts, progressing from basic data types to implementing a complete linear regression model from scratch.

## 📖 Lab 1 - Python Basics & Linear Regression

Lab 1 contains 7 progressive programs covering fundamental Python concepts:

### 01. House Data and Data Types
**File:** `01_house_data_and_datatypes.py`

Learn about basic Python data types through house information:
- Integer: House size (sq. ft.)
- Integer: House price (Lakhs)
- String: City name
- Boolean: Availability status

**Concepts:** Variables, data types, `print()`, `type()`

---

### 02. House Price Operations
**File:** `02_house_price_operations.py`

Perform arithmetic operations on house prices:
- Addition (total cost)
- Subtraction (price difference)
- Multiplication
- Division

**Concepts:** Arithmetic operators, calculations

---

### 03. House Sizes List
**File:** `03_house_sizes_list.py`

Store and access multiple house sizes using lists:
- Create a list of 5 house sizes
- Access elements by index
- Display list contents

**Concepts:** Lists, indexing, list operations

---

### 04. Estimate Price Function
**File:** `04_estimate_price_function.py`

Create a function to estimate house prices based on size:
- Formula: `Price = Size / 33.33`
- Test with multiple house sizes
- Return calculated values

**Concepts:** Functions, parameters, return values

---

### 05. Classify House Price
**File:** `05_classify_house_price.py`

Implement price classification logic:
- **Affordable:** ≤ 50 Lakhs
- **Expensive:** > 50 Lakhs
- Test with 5 different price points

**Concepts:** Conditional statements (`if-else`), decision making

---

### 06. Display House Sizes
**File:** `06_display_house_sizes.py`

Enhanced list display with formatted output:
- Display complete list
- Show individual elements with labels
- Format output for readability

**Concepts:** List iteration, formatted output

---

### 07. Linear Regression Prediction
**File:** `07_linear_regression_prediction.py`

**⭐ Complete implementation of Linear Regression from scratch**

Build a machine learning model to predict house prices:

#### 8-Step ML Process:
1. **Collect Dataset** - 5 houses with area and price data
2. **Examine Dataset** - Verify data completeness
3. **Identify Variables** - Input (Area) and Output (Price)
4. **Split Data** - 80% training (4 houses), 20% testing (1 house)
5. **Train Model** - Calculate slope (m) and intercept (b)
6. **Test Model** - Predict price for test house
7. **Evaluate** - Compare predicted vs actual price
8. **Deploy** - Predict prices for new houses

#### Mathematical Foundation:
```
Linear Regression Equation: Price = m × Area + b

Where:
m = (n·Σ(xy) - Σx·Σy) / (n·Σ(x²) - (Σx)²)
b = (Σy - m·Σx) / n
```

**Concepts:** Machine learning, linear regression, model training, prediction, error analysis

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- Basic understanding of command line/terminal
- Text editor or IDE (VS Code, PyCharm, etc.)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/shaxntanu/AI-For-Engineers.git
cd AI-For-Engineers
```

2. No additional dependencies required - all programs use Python standard library only!

## 💻 Usage

Navigate to the Lab 1 folder and run any program:

```bash
cd "Lab 1"
python 01_house_data_and_datatypes.py
```

Or run a specific program:

```bash
python "Lab 1/07_linear_regression_prediction.py"
```

### Sample Output (Program 7 - Linear Regression):
```
HOUSE PRICE PREDICTION USING LINEAR REGRESSION

Step 1: Dataset collected
Areas: [1000, 1500, 2000, 2500, 3000]
Prices: [30, 45, 60, 75, 90]

Step 5: Model trained
Slope (m): 0.03
Intercept (b): 0.0
Equation: Price = 0.03 * Area + 0.0

Step 7: Comparison
Actual price: 90 Lakhs
Predicted price: 90.0 Lakhs
Error: 0.0 Lakhs

Step 8: Predict new house prices
Area: 1800 sq. ft. → Predicted Price: 54.0 Lakhs
Area: 2200 sq. ft. → Predicted Price: 66.0 Lakhs
Area: 2800 sq. ft. → Predicted Price: 84.0 Lakhs
```

## 🎓 Learning Outcomes

After completing Lab 1, you will understand:

✅ Python fundamental data types and variables  
✅ Arithmetic operations and expressions  
✅ Lists and indexing  
✅ Function definition and usage  
✅ Conditional statements (if-else)  
✅ Basic machine learning concepts  
✅ Linear regression algorithm from scratch  
✅ Model training and testing process  
✅ Prediction and error evaluation  

## 📂 Repository Structure

```
AI-For-Engineers/
│
├── Lab 1/
│   ├── 01_house_data_and_datatypes.py
│   ├── 02_house_price_operations.py
│   ├── 03_house_sizes_list.py
│   ├── 04_estimate_price_function.py
│   ├── 05_classify_house_price.py
│   ├── 06_display_house_sizes.py
│   └── 07_linear_regression_prediction.py
│
└── README.md
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Shantanu**
- GitHub: [@shaxntanu](https://github.com/shaxntanu)

## 🌟 Show Your Support

Give a ⭐️ if this project helped you learn!

---

**Note:** These programs are designed for educational purposes to teach Python programming and machine learning fundamentals through practical examples.
