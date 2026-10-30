# AI For Engineers - Lab Repository

A collection of Python programming labs for learning AI and machine learning concepts. This repository contains practical exercises that build from basic Python programming to advanced data science techniques.

## What's Inside

**Lab 1**: Python fundamentals through house price examples  
**Lab 2**: Data preprocessing and handling missing values  
**Lab 3**: List operations for data handling  
**Lab 4**: McCulloch-Pitts neuron implementation for logic gates

**Lab 5**: PCA, K-means, and DBSCAN clustering with country data

**Lab 6**: OR function using binary inputs, bipolar targets, and perceptron training

Each lab is self-contained with complete working code, sample datasets, and detailed README files explaining the implementation.

## Visualisation Scripts

`Visualisation/` contains one Matplotlib script for each lab. Run a script from the repository root to regenerate its figure; each script saves the image into the matching lab's `figures/` folder, where that lab's README displays it.

```bash
python -m pip install matplotlib pandas scikit-learn
python Visualisation/visualise_lab1.py
python Visualisation/visualise_lab2.py
python Visualisation/visualise_lab3.py
python Visualisation/visualise_lab4.py
python Visualisation/visualise_lab5.py
python Visualisation/visualise_lab6.py
```

## Lab 1 - Python Basics

Seven programs covering Python fundamentals:

1. **Data Types** - Working with integers, strings, booleans
2. **Operations** - Basic arithmetic calculations  
3. **Lists** - Storing and accessing multiple values
4. **Functions** - Creating reusable code blocks
5. **Conditions** - Making decisions with if-else
6. **Formatted Output** - Displaying data nicely
7. **Linear Regression** - Complete ML implementation from scratch

## Lab 2 - Data Preprocessing

Working with real datasets and handling missing data:

- **Missing Value Detection** - Finding incomplete data
- **Mean Imputation** - Replacing missing values with averages
- **Data Cleaning** - Preparing datasets for analysis
- **CSV Processing** - Reading and writing data files

## Lab 3 - List Operations

Understanding Python lists for data handling:

- **List Creation** - Storing multiple house sizes
- **Iteration** - Using loops to process list elements
- **List Methods** - Counting and accessing data
- **Data Structure Basics** - Foundation for dataset handling

## Lab 4 - McCulloch-Pitts Neuron

Implementing the foundational artificial neuron model:

- **Neuron Model** - Weighted sum and threshold activation
- **Logic Gates** - AND, OR, NOT, NAND implementations
- **Truth Tables** - Understanding binary operations
- **Neural Network Foundations** - Building blocks for AI

## Lab 5 - PCA, K-Means and DBSCAN Clustering

Clustering countries using development indicators:

- **Feature Scaling** - Standardizing numeric indicators before clustering
- **PCA** - Reducing the indicators while retaining 95% of their variance
- **K-Means** - Comparing cluster counts with inertia and silhouette scores
- **DBSCAN** - Finding dense groups and identifying noise points
- **Visualization** - Plotting cluster assignments with Matplotlib

## Lab 6 - OR Function Using Perceptron Training

Training a perceptron on the binary-input OR truth table:

- **Binary Inputs** - The two input values are 0 or 1
- **Bipolar Targets** - The expected outputs are -1 or +1
- **Perceptron Learning Rule** - Updating weights and bias for mistakes
- **Training Progress** - Displaying epoch updates and the final truth table

---

Made for learning Python programming and AI concepts step by step.
