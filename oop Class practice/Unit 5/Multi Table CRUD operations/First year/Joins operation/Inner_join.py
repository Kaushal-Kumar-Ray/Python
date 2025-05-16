##table1_students.py
import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    database="first_year",
    password="Kaushal982939@")
crs=conn.cursor()
crs.execute("""
    SELECT students.prn, students.name, course.course_name, course.semester
    FROM students
    INNER JOIN course ON students.prn = course.prn
""")
#shows only those prns that are present in both tables.
for row in crs.fetchall():
    print(row)
crs.execute("commit")
conn.close()