# Lab 2 - Handling Missing Values Using Mean Imputation

## Problem Statement

Real-world datasets often contain missing values, which can cause problems when training machine learning models. This lab focuses on understanding and implementing a common technique called mean imputation to handle missing data. The task is to load a dataset with missing values, identify where the gaps are, and fill them using the mean value of each numerical column.

## Implementation Approach

The implementation uses the pandas library to efficiently handle data operations. The program follows a systematic step-by-step process to clean the dataset.

### Step 1: Load the Dataset

The program starts by loading the original dataset from a CSV file using pandas. This creates a DataFrame that makes it easy to manipulate and analyze the data. The original dataset contains some missing values represented as NaN (Not a Number).

### Step 2: Check for Missing Values

The program identifies which columns have missing values and how many are missing in each column. It uses the isnull() method combined with sum() to get a count of missing values per column. This helps understand the extent of the data quality problem.

### Step 3: Identify Numerical Columns

Mean imputation only makes sense for numerical data. The program automatically identifies which columns contain numerical data (integers or floating-point numbers) by using the select_dtypes() method. This ensures that we only apply mean imputation to appropriate columns.

### Step 4: Calculate and Apply Means

For each numerical column, the program calculates the mean value of the existing (non-missing) data. It then replaces all missing values in that column with this calculated mean. The fillna() method from pandas makes this operation straightforward. The program prints the calculated mean for each column to provide transparency about the imputation process.

### Step 5: Display the Cleaned Dataset

After imputation, the program displays the complete dataset with all missing values filled in. This allows visual verification that the operation worked correctly.

### Step 6: Verify the Results

The program performs a final check to confirm that no missing values remain in the dataset. It runs the same missing value check as in Step 2 and should now see zero missing values in all numerical columns.

### Step 7: Save the Cleaned Dataset

Finally, the program saves the cleaned dataset to a new CSV file called mean_imputed_dataset.csv. This preserves the original data while providing a clean version ready for machine learning tasks.

## Running the Program

To run the program, ensure you have pandas installed and execute:

```bash
python main.py
```

The program will display each step of the process along with intermediate results, making it easy to follow what is happening.

## Key Takeaways

Mean imputation is a simple yet effective technique for handling missing numerical data. While it has limitations (it can reduce variance and may not be appropriate for all situations), it provides a good starting point for data cleaning. This lab demonstrates the importance of data preprocessing in machine learning pipelines and shows how pandas provides powerful tools for data manipulation. Understanding how to handle missing values is a critical skill for any data scientist or machine learning engineer.
