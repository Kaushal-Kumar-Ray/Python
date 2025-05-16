#table2_course.py
import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    database="first_year",
    password="Kaushal982939@")
crs=conn.cursor()
crs.execute("create table if not exists course(prn varchar(15),course_name varchar(25), semester int)")

crs.execute("insert into course value('240205241023','B.Tech CSE AI & ML',2),('240205241017','B.Tech CSE',1)")
crs.execute("insert into course (prn,course_name) values('2402052410000','B.Tech Civil')")  

crs.execute("commit")
conn.close()