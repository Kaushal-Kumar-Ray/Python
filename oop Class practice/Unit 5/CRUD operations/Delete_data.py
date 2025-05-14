import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    database="practice",
    password="Kaushal982939@"
)
crs=conn.cursor()
crs.execute("delete from students where prn='240205231028'")
crs.execute("commit")
#crs.execute("truncate students")
#crs.execute("droptable students")
crs.execute("select * from students")
for row in crs: 
    print(row)
    
conn.close() 
