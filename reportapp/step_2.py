import sqlite3

# Step 1 :: Connect to the test database (or create it if it doesn't exist)
conn = sqlite3.connect("test_db.db")
cursor = conn.cursor()

# Step 2 :: Get the database schema
schema = cursor.execute("PRAGMA table_info(employees)").fetchall()
schema_str = "CREATE TABLE EMPLOYEES (\n" + "\n".join([f"{col[1]} {col[2]}" for col in schema]) + "\n)"
print("===== Database Schema =====")
print(schema_str)

# Step 3 :: Question
question = "ขอ employee ทั้งหมด"

# Step 4 :: Connect to OpenAI
from openai import OpenAI
client = OpenAI()
MODEL_NAME = "gpt-4o"

def ask_openai(question, schema):
    prompt = f"""Here is the schema for a database:
    {schema}
    Given this schema, can you output a SQL query to answer the following question? 
    Only output the SQL query and do not show additional information.

    Question: {question}
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    return response.choices[0].message.content

# Step 5 :: Ask OpenAI for the SQL query
print("\n===== Question =====")
print(question)
sql_query = ask_openai(question, schema_str)
print("\n===== Generated SQL Query =====")
print("SQL Query:")
print(sql_query)