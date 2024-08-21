Supermarket Sales Analysis

Project Overview
This project involves analyzing sales data from a supermarket to gain insights into customer behavior, product performance, and sales trends. The dataset used contains detailed information on transactions across different branches, including product lines, customer demographics, and sales amounts.

Dataset
Name: Supermarket Sales Dataset
Source: Kaggle
Description: The dataset includes sales data for a supermarket, with fields such as Invoice ID, Branch, City, Customer Type, Gender, Product Line, Total, Date, Payment Method, and more.
Tools and Technologies
Programming Language: Python

Libraries Used:
pandas for data manipulation and analysis
matplotlib and seaborn for data visualization
sqlite3 for database management and SQL queries
Development Environment: Visual Studio Code with Jupyter Notebooks and SQLite extensions

Project Steps
1)Data Loading and Exploration:
  Loaded the dataset into a Pandas DataFrame.
  Conducted an initial exploration to understand the data structure, check for missing values, and calculate basic statistics.
2)Data Cleaning:
  Handled missing values and ensured data types were correct.
  Removed duplicate records to maintain data integrity.
3)Exploratory Data Analysis (EDA):
  Performed descriptive statistical analysis to calculate total and average sales.
  Created visualizations to explore sales trends over time, sales by product line, and sales distribution across product categories.
4)SQL Integration:
  Loaded the cleaned dataset into an SQLite database.
  Executed SQL queries to analyze sales by product line and track sales trends over time.
5)Visualization of SQL Results:
  Retrieved SQL query results and visualized them using Python libraries to provide additional insights.

Key Insights
Product Line Performance: The analysis revealed which product lines generated the highest and lowest total sales, helping to identify top-performing products.
Sales Trends: Daily sales trends were visualized, showing patterns over time, which can be useful for understanding peak shopping periods.
Customer Behavior: Analysis of customer demographics (e.g., gender, customer type) provided insights into the customer base, which could inform targeted marketing strategies.

How to Run the Project
  Clone the Repository:
            git clone https://github.com/your-username/supermarket-sales-analysis.git
  Install Required Python Libraries:
            pip install pandas matplotlib seaborn sqlite3
Run the Jupyter Notebook:
            Open supermarket_sales_analysis.ipynb in Jupyter Notebook and run the cells to perform the analysis.

Conclusion

This project provides a comprehensive analysis of supermarket sales data, leveraging both Python and SQL for data exploration and visualization. The insights derived can help inform business decisions, optimize operations, and improve customer engagement.
