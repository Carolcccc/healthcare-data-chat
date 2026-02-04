"""
Data Preparation Script for Healthcare Dataset
Cleans and prepares the dataset for optimal AI agent performance
"""

import pandas as pd
import numpy as np
from datetime import datetime

def clean_healthcare_data(input_file='healthcare_dataset.csv', output_file='healthcare_dataset_cleaned.csv'):
    """
    Clean and prepare healthcare dataset for AI agent
    
    Steps:
    1. Load the raw CSV
    2. Handle missing values
    3. Standardize date formats
    4. Clean text fields
    5. Remove duplicates
    6. Validate data types
    7. Save cleaned version
    """
    
    print("🔄 Starting data cleaning process...")
    print(f"📂 Loading: {input_file}")
    
    # Load dataset
    df = pd.read_csv(input_file)
    print(f"✅ Loaded {len(df)} records with {len(df.columns)} columns")
    
    # Display initial info
    print("\n📊 Initial Data Info:")
    print(f"   - Shape: {df.shape}")
    print(f"   - Columns: {list(df.columns)}")
    print(f"   - Missing values: {df.isnull().sum().sum()}")
    
    # 1. Handle missing values
    print("\n🧹 Cleaning missing values...")
    initial_nulls = df.isnull().sum().sum()
    
    # Fill numeric columns with median
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df[col].isnull().any():
            df[col].fillna(df[col].median(), inplace=True)
            print(f"   - Filled {col} with median")
    
    # Fill categorical columns with mode or 'Unknown'
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        if df[col].isnull().any():
            mode_val = df[col].mode()
            if len(mode_val) > 0:
                df[col].fillna(mode_val[0], inplace=True)
                print(f"   - Filled {col} with mode")
            else:
                df[col].fillna('Unknown', inplace=True)
                print(f"   - Filled {col} with 'Unknown'")
    
    print(f"   ✓ Cleaned {initial_nulls} missing values")
    
    # 2. Standardize date formats
    print("\n📅 Standardizing date formats...")
    date_columns = [col for col in df.columns if 'date' in col.lower() or 'Date' in col]
    for col in date_columns:
        try:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            # Convert to standard format YYYY-MM-DD
            df[col] = df[col].dt.strftime('%Y-%m-%d')
            print(f"   - Standardized {col}")
        except Exception as e:
            print(f"   ⚠️  Could not standardize {col}: {e}")
    
    # 3. Clean text fields - remove extra whitespace
    print("\n✂️  Trimming text fields...")
    for col in categorical_cols:
        if df[col].dtype == 'object':
            df[col] = df[col].str.strip()
    
    # 4. Remove duplicate rows
    print("\n🔍 Checking for duplicates...")
    initial_rows = len(df)
    df = df.drop_duplicates()
    duplicates_removed = initial_rows - len(df)
    if duplicates_removed > 0:
        print(f"   ✓ Removed {duplicates_removed} duplicate rows")
    else:
        print(f"   ✓ No duplicates found")
    
    # 5. Sort by a logical column if exists
    if 'Name' in df.columns:
        df = df.sort_values('Name').reset_index(drop=True)
        print("\n📑 Sorted by Name")
    
    # 6. Final validation
    print("\n✅ Final Data Info:")
    print(f"   - Shape: {df.shape}")
    print(f"   - Missing values: {df.isnull().sum().sum()}")
    print(f"   - Data types:")
    for col in df.columns:
        print(f"      • {col}: {df[col].dtype}")
    
    # 7. Save cleaned dataset
    df.to_csv(output_file, index=False)
    print(f"\n💾 Saved cleaned dataset to: {output_file}")
    
    # Display sample
    print("\n👀 Sample of cleaned data (first 3 rows):")
    print(df.head(3))
    
    print("\n🎉 Data cleaning complete!")
    return df

if __name__ == "__main__":
    # Run the cleaning process
    cleaned_df = clean_healthcare_data()
    
    # Display summary statistics
    print("\n📈 Summary Statistics:")
    print(cleaned_df.describe())
