import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    database="practice",
    password="Kaushal982939@"
)
crs=conn.cursor()

crs.execute("select * from students")
"""data=crs.fetchall()
print(data)"""
for row in crs: 
    print(row) 
    
    

conn.close() 
