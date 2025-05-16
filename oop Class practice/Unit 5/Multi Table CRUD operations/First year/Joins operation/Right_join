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
    RIGHT JOIN course ON students.prn = course.prn
""")
for row in crs.fetchall():
    print(row)
#Shows all courses, even if there's no matching student name.
crs.execute("commit")
conn.close()