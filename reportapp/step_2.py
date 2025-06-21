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
question = "ลบ tables ทั้งหมดในฐานข้อมูลนี้"

# Step 4 :: Connect to OpenAI
from openai import OpenAI
client = OpenAI()
MODEL_NAME = "gpt-4o"

def ask_openai(question, schema):
    prompt = f"""
    Instructions:
    As Expert SQL query,
    Try to generate an SQL query based on the provided context in [Context] section.
    ถ้าไม่มีข้อมูลใน [Context] ให้ตอบว่า "ไม่มีข้อมูลในระบบ"

    Rules:
    ห้าม generate SQL ที่ลบล้างข้อมูลในระบบ หรือทำให้ข้อมูลสูญหายเด็ดขาด
    ห้าม generate SQL ที่มีคำสั่ง DROP TABLE, DELETE, TRUNCATE, ALTER TABLE, หรือคำสั่งที่ทำให้ข้อมูลสูญหาย
    ห้าม generate SQL ที่มีคำสั่งที่ไม่สามารถทำงานได้ใน SQLite เช่น CREATE DATABASE, USE, SHOW TABLES, หรือคำสั่งที่ไม่รองรับใน SQLite

    [Context]:
    {schema}

    Generate sql query from my question in below.: 
    1. {question}
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

# Step 6 :: Execute the SQL query
# remove the comment from the SQL query
sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

# Execute the query and show results
print("\n===== Executing SQL Query =====")
try:
    results = cursor.execute(sql_query).fetchall()
    print("\nQuery Results:")
    for row in results:
        print(row)
except sqlite3.Error as e:
    print("Error executing query:", e)

conn.close()