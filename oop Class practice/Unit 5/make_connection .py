import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    database="practice",
    user="root",
    password="Kaushal982939@"
    )
print("Connection established")
conn.close()