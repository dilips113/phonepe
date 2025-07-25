import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# STEP 1: Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",             # change if different
    password="Sakthi2004@cit",  # replace with your MySQL password
    database="phonepe"
)

# STEP 2: Read Data from aggregated_transaction table
query = """
SELECT state, year, quarter, transaction_type, transaction_count, transaction_amount
FROM aggregated_transaction
"""
df = pd.read_sql(query, connection)

# Display top few rows
print("Sample Data:")
print(df.head())

# STEP 3: Pie Chart of Transaction Types (Overall)
plt.figure(figsize=(8, 6))
type_data = df.groupby('transaction_type')['transaction_amount'].sum().sort_values(ascending=False)
plt.pie(type_data, labels=type_data.index, autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Transaction Amount by Type")
plt.axis('equal')
plt.show()

# STEP 4: Line Chart of Quarterly Transaction Trends (All India)
quarterly_trend = df.groupby(['year', 'quarter'])['transaction_amount'].sum().reset_index()
quarterly_trend['year_quarter'] = quarterly_trend['year'].astype(str) + " Q" + quarterly_trend['quarter'].astype(str)

plt.figure(figsize=(10, 6))
sns.lineplot(x='year_quarter', y='transaction_amount', data=quarterly_trend, marker='o')
plt.xticks(rotation=45)
plt.title("Quarterly Transaction Amount Trend (All India)")
plt.xlabel("Year-Quarter")
plt.ylabel("Total Transaction Amount")
plt.tight_layout()
plt.show()

# Close MySQL connection
connection.close()
