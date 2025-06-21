import sqlite3
from softnix import call_api

# Step 1 :: Connect to the test database (or create it if it doesn't exist)
conn = sqlite3.connect("test_db.db")
cursor = conn.cursor()

# Step 2 :: Get the database schema
schema = cursor.execute("PRAGMA table_info(employees)").fetchall()
schema_str = "CREATE TABLE EMPLOYEES (\n" + "\n".join([f"{col[1]} {col[2]}" for col in schema]) + "\n)"
print("===== Database Schema =====")
print(schema_str)

# Step 3 :: Question
question = "ข้อมูลพนักงานทั้งหมดที่มีเงินเดือนมากกว่า 50000 บาท"

# Step 4 :: Connect to Softnix API
def ask_softnix(schema, prompt):
    """
    Asks the Softnix API for a SQL query based on the question and schema.
    """
    response = call_api(schema, prompt)
    return response["answer"]

# Step 5 :: Ask OpenAI for the SQL query
print("\n===== Question =====")
print(question)
sql_query = ask_softnix(schema_str, question)
print("\n===== Generated SQL Query =====")
print("SQL Query:")
print(sql_query)

# Step 6 :: Execute the SQL query
print("\n===== Executing SQL Query =====")
try:
    results = cursor.execute(sql_query).fetchall()
    print("\nQuery Results:")
    for row in results:
        print(row)
except sqlite3.Error as e:
    print("Error executing query:", e)

conn.close()