import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    database="first_year",
    password="Kaushal982939@")
crs=conn.cursor()


#Inner join operation
print("Inner join operation")
crs.execute("""
    SELECT students.prn, students.name, course.course_name, course.semester FROM students
    inner join course ON students.prn = course.prn
""")
for row in crs.fetchall():
    print(row)
 #shows only those prns that are present in both tables.
crs.execute("commit")


#left join operation
print("")
print("Left join operation")
crs.execute("""
    SELECT students.prn, students.name, course.course_name, course.semester
    FROM students
    LEFT JOIN course ON students.prn = course.prn
""")
for row in crs.fetchall():
    print(row)
#Shows all students, including the one without a name, matched with course if available.
crs.execute("commit")


#right join operation
print("")
print("Right join operation")
crs.execute("""
    SELECT students.prn, students.name, course.course_name, course.semester
    FROM students
    RIGHT JOIN course ON students.prn = course.prn
""")
for row in crs.fetchall():
    print(row)
#Shows all courses, even if there's no matching student name.
crs.execute("commit")


#cross join operation
print("")
print("Cross join operation")
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