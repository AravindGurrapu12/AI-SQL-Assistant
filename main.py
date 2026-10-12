# from dotenv import load_dotenv
# import os
#
# load_dotenv()
#
# api_key = os.getenv("GEMINI_API_KEY")
#
# print("API key loaded:", api_key is not None)
# from dotenv import load_dotenv
# from google import genai
# import os
#
# load_dotenv()
#
# api_key = os.getenv("GEMINI_API_KEY")
#
# client = genai.Client(api_key=api_key)
#
# response = client.models.generate_content(
#     model="gemini-3.5-flash-lite",
#     contents="Explain what SQL is in one simple sentence."
# )
#
# print(response.text)
from dotenv import load_dotenv
from google import genai
import os

# load_dotenv()
#
# api_key = os.getenv("GEMINI_API_KEY")
#
# client = genai.Client(api_key=api_key)
#
# schema = """
# Database: ITEMPLOYES
# Table: ITemployee
#
# Columns:
# id
# name
# department
# city
# age
# salary
# """
#
# question = "Show all employees whose salary is greater than 50000."
#
# prompt = f"""
# You are an SQL assistant.
#
# Here is the database structure:
#
# {schema}
#
# User question:
# {question}
#
# Generate only the SQL query.
# Do not explain the query.
# """
#
# response = client.models.generate_content(
#     model="gemini-3.5-flash-lite",
#     contents=prompt
# )
#
# print("Generated SQL:")
# print(response.text)
# from dotenv import load_dotenv
# import mysql.connector
# import os
#
# load_dotenv()
#
# connection = mysql.connector.connect(
#     host=os.getenv("MYSQL_HOST"),
#     user=os.getenv("MYSQL_USER"),
#     password=os.getenv("MYSQL_PASSWORD"),
#     database=os.getenv("MYSQL_DATABASE")
# )
#
# print("Connected to MySQL successfully!")
#
# connection.close()
# from dotenv import load_dotenv
# import mysql.connector
# import os
#
# load_dotenv()
#
# connection = mysql.connector.connect(
#     host=os.getenv("MYSQL_HOST"),
#     user=os.getenv("MYSQL_USER"),
#     password=os.getenv("MYSQL_PASSWORD"),
#     database=os.getenv("MYSQL_DATABASE")
# )
#
# cursor = connection.cursor()
#
# query = "SELECT * FROM ITemployee;"
#
# cursor.execute(query)
#
# results = cursor.fetchall()
#
# for row in results:
#     print(row)
#
# cursor.close()
# connection.close()
from dotenv import load_dotenv
from google import genai
import mysql.connector
import os

load_dotenv()

# -------------------------
# 1. Connect to Gemini
# -------------------------

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


# -------------------------
# 2. Database information
# -------------------------

schema = """
Database: ITEMPLOYES
Table: ITemployee

Columns:
id
name
department
salary
age
city
"""

question = input("Ask your question: ")


# -------------------------
# 3. Ask Gemini to generate SQL
# -------------------------

prompt = f"""
You are an SQL assistant.

Database structure:

{schema}

User question:
{question}

Generate only the SQL query.
Do not explain the query.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

sql_query = response.text.strip()

if sql_query.startswith("```"):
    sql_query = sql_query.replace("```sql", "")
    sql_query = sql_query.replace("```", "")
    sql_query = sql_query.strip()

print("Generated SQL:")
print(sql_query)


# -------------------------
# 4. Connect to MySQL
# -------------------------

connection = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

cursor = connection.cursor()


# -------------------------
# 5. Execute Gemini's SQL
# -------------------------

cursor.execute(sql_query)

results = cursor.fetchall()
# Convert database rows into text
results_text = "\n".join(str(row) for row in results)

# Ask Gemini to explain the database results
answer_prompt = f"""
You are an AI SQL Assistant.

User question:
{question}

Database results:
{results_text}

Answer the user's question clearly using only the database results.
Do not invent information.
If there are no results, say that no matching records were found.
"""

answer_response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=answer_prompt
)

print("\nAssistant:")
print(answer_response.text)

# -------------------------
# 6. Display results
# -------------------------

# print("\nDatabase Results:")
#
# for row in results:
#     print(row)


# -------------------------
# 7. Close connection
# -------------------------

cursor.close()
connection.close()