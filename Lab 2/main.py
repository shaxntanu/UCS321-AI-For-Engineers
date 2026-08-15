# Program: Handling Missing Values Using Mean Imputation

import pandas as pd

print ("HANDLING MISSING VALUES USING MEAN")
print ()

# Step 1: Load the original dataset
df_original = pd.read_csv('original_dataset.csv')

print ("Step 1: Original dataset loaded")
print ("Dataset:")
print (df_original)
print ()

# Step 2: Check for missing values
print ("Step 2: Checking for missing values")
missing_values = df_original.isnull().sum()
print ("Missing values count:")
print (missing_values)
print ()

# Step 3: Identify numerical columns
numerical_cols = df_original.select_dtypes(include=['float64', 'int64']).columns.tolist()
print ("Step 3: Numerical columns identified")
print ("Columns:", numerical_cols)
print ()

# Step 4: Calculate means for numerical columns
print ("Step 4: Calculating column means")
df_imputed = df_original.copy()

for col in numerical_cols:
    mean_value = df_imputed[col].mean()
    print (col, "mean:", round(mean_value, 2))
    
    # Replace missing values with mean
    df_imputed[col] = df_imputed[col].fillna(mean_value)

print ()

# Step 5: Display final dataset
print ("Step 5: Final dataset after mean imputation")
print (df_imputed)
print ()

# Step 6: Verify missing values are handled
print ("Step 6: Verification")
final_missing = df_imputed.isnull().sum()
print ("Missing values after imputation:")
print (final_missing)
print ()

# Step 7: Save the cleaned dataset
df_imputed.to_csv('mean_imputed_dataset.csv', index=False)
print ("Step 7: Cleaned dataset saved as 'mean_imputed_dataset.csv'")
print ()
print ("Missing value handling completed successfully!")