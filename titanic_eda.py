import pandas as pd
import numpy as np

def main():
    # Step 1: Load the dataset using Pandas
    print("--- 1. Loading Titanic Dataset ---")
    # Using a widely available CSV link for the standard Titanic dataset
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    titanic_df = pd.read_csv(url)
    print("Dataset loaded successfully.\n")

    # Step 6: Display the shape and dimensions of the dataset
    print("--- 6. Shape and Dimensions ---")
    print(f"Number of rows: {titanic_df.shape[0]}")
    print(f"Number of columns: {titanic_df.shape[1]}")
    print(f"Dimensions: {titanic_df.ndim}\n")

    # Step 2: Display the data structure using .info() and .describe() methods
    print("--- 2. Data Structure (.info) ---")
    titanic_df.info()
    print("\n--- Statistical Summary (.describe) ---")
    # include='all' provides descriptive statistics for both categorical and numerical columns
    print(titanic_df.describe(include='all'))
    print("\n")

    # Step 7: List the data types (int, float, object) of all columns
    print("--- 7. Data Types ---")
    print(titanic_df.dtypes)
    print("\n")

    # Step 3: Identify and separate Numerical and Categorical variables
    print("--- 3. Separating Numerical and Categorical Variables ---")
    # Select columns by generic data types
    numerical_cols = titanic_df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = titanic_df.select_dtypes(exclude=[np.number]).columns.tolist()
    
    print(f"Numerical variables ({len(numerical_cols)}): {numerical_cols}")
    print(f"Categorical variables ({len(categorical_cols)}): {categorical_cols}\n")

    # Step 4: Check for missing values in all columns
    print("--- 4. Missing Values ---")
    missing_values = titanic_df.isnull().sum()
    print("Missing values across all columns:")
    print(missing_values)
    print("\n")

    # Step 5: Identify unique values in each categorical column
    print("--- 5. Unique Values in Categorical Columns ---")
    for col in categorical_cols:
        unique_vals = titanic_df[col].unique()
        num_unique = titanic_df[col].nunique(dropna=False)
        print(f"Column '{col}' has {num_unique} unique values:")
        # Truncate output if there are too many unique values (like in 'Name' or 'Ticket')
        if num_unique > 20: 
            print(f"  {unique_vals[:20]} ... (truncated)")
        else:
            print(f"  {unique_vals}")
    print("\n")

    # Final Step: Brief summary of the data structure explaining findings (Internship Deliverable)
    print("="*60)
    print("--- Dataset Summary (Internship Deliverable) ---")
    print("="*60)
    summary = """
Summary of the Titanic Dataset Structure:
- Observations & Features: The dataset consists of 891 passenger records and 12 features, including the target variable ('Survived').
- Variable Types: 
  * Numerical features include Age, Fare, SibSp (siblings/spouses), and Parch (parents/children). 
  * Categorical/Text features include attributes like Sex, Cabin, Embarked, text identifiers (Name, Ticket), and ordinal identifiers (Pclass).
- Missing Data: There are missing values in the 'Age' (177 missing), 'Cabin' (687 missing), and 'Embarked' (2 missing) columns. 
  * 'Cabin' has a significant amount of missing data (~77%), which might require dropping the column or specialized imputation.
  * 'Age' misses about ~20% of its values and will require basic imputation (e.g., mean/median) before modeling.
- Data Types: The dataset contains a mix of integers (int64), floating-point numbers (float64), and strings/mixed types (object).
- Statistical Insights: Only about 38.4% of passengers in this set survived. The average age is around 29.7 years. Fare has a very large spread (max 512.33 vs 75th percentile 31.00), indicating a strong right-skewed distribution which might require transformation.
"""
    print(summary)


if __name__ == "__main__":
    main()
