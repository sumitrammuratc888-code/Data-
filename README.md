# Data-
Task 1: Understanding Dataset & Data Types
*Internship:* AI & ML Internship
*Organization:* Edutech Solution
*Project Name:* DataInsight: EDA Fundamentals
## 📌 Project Overview
This project focuses on the initial phase of Exploratory Data Analysis (EDA). The goal is to load a standard dataset, inspect its internal structure, identify various data types, and document missing values to build a strong foundation for future machine learning models.
## 🛠️ Tools & Libraries
 * *Language:* Python
 * *Libraries:* Pandas, NumPy, Seaborn (for dataset loading)
 * *Environment:* VS Code / Jupyter Notebook
## 📊 Dataset Description
For this task, I utilized the *Titanic Dataset*, which provides information about the passengers on board the Titanic.
 * *Total Rows:* 891
 * *Total Columns:* 12
 * *Target Variable:* Survived
## 🔍 Data Exploration Steps
 1. *Data Loading:* Imported the dataset using Pandas.
 2. *Structural Analysis:* Used .info() to understand the schema and .describe() for statistical summaries.
 3. *Data Types Identification:*
   * *Numerical:* Age, Fare, SibSp, Parch (int64, float64).
   * *Categorical:* Sex, Embarked, Pclass, Survived (object, int64).
 4. *Missing Value Detection:* Identified null values in 'Age', 'Cabin', and 'Embarked' columns.
 5. *Unique Value Check:* Calculated unique entries for categorical variables to understand data diversity.
## 💡 Key Findings (Brief Summary)
 * The dataset contains a mix of structured numerical and categorical data.
 * The *'Cabin'* column has a high percentage of missing values (nearly 77%), which may require dropping or specialized imputation.
 * The *'Age'* column is missing approximately 20% of its data, which is critical for survival analysis.
 * Numerical features like *'Fare'* show a wide range, indicating the need for potential scaling in future tasks.
## 🚀 How to Run the Script
 1. Clone this repository.
 2. Ensure you have Python installed.
 3. Install dependencies: pip install pandas numpy seaborn
 4. Run the script: python titanic_eda.py
### *Submission Checklist:*
 * [x] Python Script (titanic_eda.py)
 * [x] Dataset Analysis Summary (Included in this README)
 * [x] Terminal Output Screenshots (Added to the repository)
