import os
import json
import mysql.connector

# Step 1: Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",         # Replace with your MySQL username
    password="Sakthi2004@cit",     # Replace with your MySQL password
    database="phonepe"
)
cursor = conn.cursor()

# Step 2: Define path to JSON files
path = "pulse/data/aggregated/transaction/country/india/state/"

# Step 3: Loop through each file and extract data
for state in os.listdir(path):
    state_path = os.path.join(path, state)
    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)
        for quarter_file in os.listdir(year_path):
            if quarter_file.endswith('.json'):
                file_path = os.path.join(year_path, quarter_file)
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    
                    try:
                        for tx in data['data']['transactionData']:
                            name = tx['name']
                            count = tx['paymentInstruments'][0]['count']
                            amount = tx['paymentInstruments'][0]['amount']
                            quarter = quarter_file.replace('.json', '')

                            # Step 4: Insert data into MySQL table
                            query = """
                            INSERT INTO aggregated_transaction (state, year, quarter, transaction_type, transaction_count, transaction_amount)
                            VALUES (%s, %s, %s, %s, %s, %s)
                            """
                            values = (state, year, quarter, name, count, amount)
                            cursor.execute(query, values)
                    except:
                        pass

# Step 5: Commit and close
conn.commit()
cursor.close()
conn.close()
print("Data inserted successfully!")
