import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    database="practice",
    password="Kaushal982939@"
)
crs=conn.cursor()

crs.execute("update students set name='Akash' where prn='240205241024'")
crs.execute("commit")
crs.execute("select * from students")  
  
for row in crs:
    print(row)
    
conn.close() 
