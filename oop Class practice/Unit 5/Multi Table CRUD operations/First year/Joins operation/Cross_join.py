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
    CROSS JOIN course
""")
for row in crs.fetchall():
    print(row)
#Shows all combinations of students and courses.
#Output: You’ll get 3 students × 3 courses = 9 rows (cartesian product).
crs.execute("commit")
conn.close()