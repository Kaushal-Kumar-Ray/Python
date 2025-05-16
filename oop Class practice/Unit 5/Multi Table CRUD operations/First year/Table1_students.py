##table1_students.py
import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    database="first_year",
    password="Kaushal982939@")
crs=conn.cursor()
crs.execute("create table if not exists students(prn varchar(15),name varchar(25))")
crs.execute("insert into students value('240205241023', 'Kaushal'),('240205241017','Adarsh')")
crs.execute("insert into students (prn) values('2402052410000')")
crs.execute("commit")
conn.close()