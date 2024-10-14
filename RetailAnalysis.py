# Supermarket Sales Analysis Project
# Author: Yvonne Mwangi
# Date: 3th September 2024

# Step 1: Import Necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# Step 2: Load the Dataset
# Replace 'path_to_your_file.csv' with the actual file path
file_path = 'supermarket_sales.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())

# Step 3: Explore the Data
# Check the structure of the dataset
print(data.info())

# Check for missing values
print(data.isnull().sum())

# Basic statistics of numerical columns
print(data.describe())

# Step 4: Clean the Data
# Handle Missing Values (if any)
data_cleaned = data.dropna()

# Convert 'Date' column to datetime (if applicable)
data_cleaned['Date'] = pd.to_datetime(data_cleaned['Date'])

# Remove duplicates
data_cleaned = data_cleaned.drop_duplicates()

# Step 5: Perform Exploratory Data Analysis (EDA)

# Calculate total and average sales
total_sales = data_cleaned['Total'].sum()
average_sales = data_cleaned['Total'].mean()

print(f"Total Sales: {total_sales}")
print(f"Average Sales per Transaction: {average_sales}")

# Bar Chart: Total Sales by Product Line
product_sales = data_cleaned.groupby('Product line')['Total'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=product_sales.values, y=product_sales.index)
plt.title('Total Sales by Product Line')
plt.xlabel('Sales Amount')
plt.ylabel('Product Line')
plt.show()

# Line Plot: Sales Over Time
daily_sales = data_cleaned.groupby('Date')['Total'].sum()
plt.figure(figsize=(10, 6))
plt.plot(daily_sales.index, daily_sales.values, marker='o')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales Amount')
plt.show()

# Pie Chart: Sales Distribution by Product Line
category_sales = data_cleaned.groupby('Product line')['Total'].sum()
plt.figure(figsize=(8, 8))
plt.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=140)
plt.title('Sales Distribution by Product Line')
plt.show()

# Step 6: Use SQL to Analyze the Data
# Create an SQLite database and load the dataset into it
conn = sqlite3.connect('supermarket_sales.db')
cursor = conn.cursor()

# Load the cleaned data into a SQL table
data_cleaned.to_sql('SalesData', conn, if_exists='replace', index=False)

# Example SQL Query 1: Total Sales per Product Line
query = "SELECT `Product line`, SUM(Total) as TotalSales FROM SalesData GROUP BY `Product line` ORDER BY TotalSales DESC"
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)

# Example SQL Query 2: Sales Over Time
query = "SELECT Date, SUM(Total) as DailySales FROM SalesData GROUP BY Date ORDER BY Date"
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)

# Step 7: Visualize SQL Query Results in Python

# Retrieve SQL Query Results and convert them to a DataFrame
df_product_sales = pd.read_sql_query(query, conn)

# Display the DataFrame
print(df_product_sales.head())

# (Optional) Create additional visualizations as needed

# Step 8: Summarize Your Findings
# (You can write a summary report or include notes here)
