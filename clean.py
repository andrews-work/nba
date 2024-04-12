# clean.py

import pandas as pd

def clean_data(data):
    # Step 1: Inspect data
    print("Data Overview:")
    print(data.head())

    # Step 2: Check for missing values
    print("\nMissing Values:")
    print(data.isnull().sum())

    # Step 3: Handle missing values (if any)
    cleaned_data = data.dropna()

    # Step 4: Check for duplicates
    print("\nDuplicate Records:")
    print(cleaned_data.duplicated().sum())

    # Step 5: Remove duplicates (if any)
    cleaned_data = cleaned_data.drop_duplicates()

    # Step 6: Check data types
    print("\nData Types:")
    print(cleaned_data.dtypes)

    # Additional Step: Handle outliers (if needed)
    # ...

    # Remove whitespace from column names
    cleaned_data.columns = cleaned_data.columns.str.strip()

    return cleaned_data
