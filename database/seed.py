import psycopg2
import json

# Database connection details
conn = psycopg2.connect(
    dbname="codecraft",
    user="postgres",
    password="password",
    host="db"
)

cursor = conn.cursor()

# Insert initial data
quests = [
    {
        "name": "Automate the Bakery",
        "description": "Write a Python script to automate the production of bread in the city's bakery.",
        "code_template": "# Define variables for ingredients\nflour = 0\nwater = 0\nyeast = 0\n# Write your code here"
    }
]

for quest in quests:
    cursor.execute(
        "INSERT INTO quests (name, description, code_template) VALUES (%s, %s, %s)",
        (quest["name"], quest["description"], quest["code_template"])
    )

conn.commit()
cursor.close()
conn.close()
