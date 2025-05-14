import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    database="practice",
    user="root",
    password="Kaushal982939@"
    )

crs=conn.cursor()
crs.execute("create table if not exists students(name varchar(25),prn varchar(12),branch varchar(25))")
#crs.execute("insert into students values('Kaushal','240205241023','B.Tech CSE (AI & ML)'),('Raju','240205241033','B.Tech CSE (AI & ML)'),('Adarsh','240205241017','B.Tech CSE (AI & ML)'),('Sadish','240205241000','B.Tech CSE (AI & ML)'),('Chandrahash','240205241026','B.Tech CSE (AI & ML)')")
crs.execute("insert into students values('Kaushal','240205241023','B.Tech CSE (AI & ML)')")
crs.execute("insert into students values('Raju','240205241033','B.Tech CSE (AI & ML)')")
crs.execute("insert into students values('Adarsh','240205241017','B.Tech CSE (AI & ML)')")
crs.execute("insert into students values('Sadish','240205241024','B.Tech CSE (AI & ML)')")
crs.execute("insert into students values('Chandrahash','240205241026','B.Tech CSE (AI & ML)')")
crs.execute("insert into students values('Satyam','240205231028','B.Tech CSE')")
#crs.execute("delete  from students")
conn.commit()
conn.close()






"""crs=con.cursor()
crs.execute("create table student(Prn int(10),Name varchar(20),Age int(3),Branch varchar(20))")
crs.execute("commit")
crs.execute("insert into student values(1,'Kaushal',22,'CSE')")
crs.execute("insert into student values(2,'Amit',23,'IT')")
crs.execute("insert into student values(3,'Adarsh',24,'CSE')")


crs.execute("select * from student")
data=crs.fetchall()
print(data)"""
