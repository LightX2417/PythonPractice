# Create a student enrollment system where you can:
# Add students with their name, age, and major.
# Enroll students in courses with course name and credits.
# View all students and their enrolled courses.

import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="example_db",
    user="example_user",
    password="example_password",
    host="localhost",
    port="5432",
)
cursor = conn.cursor()

# Create tables
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name TEXT,
    age INTEGER,
    major TEXT
)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS courses (
    id SERIAL PRIMARY KEY,
    course_name TEXT,
    credits INTEGER
)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS enrollments (
    student_id INTEGER REFERENCES students(id),
    course_id INTEGER REFERENCES courses(id),
    PRIMARY KEY (student_id, course_id)
)
"""
)
conn.commit()


# Add a student
def add_student(name, age, major):
    cursor.execute(
        """
    INSERT INTO students (name, age, major)
    VALUES (%s, %s, %s)
    """,
        (name, age, major),
    )
    conn.commit()


# Add a course
def add_course(course_name, credits):
    cursor.execute(
        """
    INSERT INTO courses (course_name, credits)
    VALUES (%s, %s)
    """,
        (course_name, credits),
    )
    conn.commit()


# Enroll a student in a course
def enroll_student(student_id, course_id):
    cursor.execute(
        """
    INSERT INTO enrollments (student_id, course_id)
    VALUES (%s, %s)
    """,
        (student_id, course_id),
    )
    conn.commit()


# View all students with their courses
def view_students_and_courses():
    cursor.execute(
        """
    SELECT students.name, courses.course_name
    FROM students
    JOIN enrollments ON students.id = enrollments.student_id
    JOIN courses ON enrollments.course_id = courses.id
    """
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)


# Example usage
add_student("John Doe", 20, "Computer Science")
add_student("Jane Smith", 22, "Mathematics")
add_course("Intro to Programming", 3)
add_course("Calculus I", 4)
enroll_student(1, 1)
enroll_student(2, 2)
view_students_and_courses()

# Close the connection
cursor.close()
conn.close()
