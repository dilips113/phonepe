import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up page
st.set_page_config(page_title="PhonePe Insights", layout="wide")
st.title("📊 PhonePe Transaction Dashboard")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sakthi2004@cit",  # replace with your MySQL password
    database="phonepe"
)

# Load Data
query = "SELECT * FROM aggregated_transaction"
df = pd.read_sql(query, conn)

# Filter Sidebar
st.sidebar.header("Filter")
years = sorted(df["year"].unique())
selected_year = st.sidebar.selectbox("Select Year", years)

quarters = sorted(df[df["year"] == selected_year]["quarter"].unique())
selected_quarter = st.sidebar.selectbox("Select Quarter", quarters)

filtered_df = df[(df["year"] == selected_year) & (df["quarter"] == selected_quarter)]

# Pie Chart
st.subheader("Transaction Type Distribution")
type_data = filtered_df.groupby("transaction_type")["transaction_amount"].sum()
fig1, ax1 = plt.subplots()
ax1.pie(type_data, labels=type_data.index, autopct="%1.1f%%", startangle=140)
ax1.axis("equal")
st.pyplot(fig1)

# Line Chart for Trend
st.subheader("Quarterly Trend of Transactions")
trend_df = df.groupby(["year", "quarter"])["transaction_amount"].sum().reset_index()
trend_df["label"] = trend_df["year"].astype(str) + " Q" + trend_df["quarter"].astype(str)
fig2, ax2 = plt.subplots()
sns.lineplot(data=trend_df, x="label", y="transaction_amount", marker="o", ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

# Table View
st.subheader("Raw Data Table")
st.dataframe(filtered_df)

# Close Connection
conn.close()
