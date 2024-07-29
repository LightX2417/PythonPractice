import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="university_db",
    user="university_user",
    password="university_password",
    host="localhost",
    port="5432",
)
cursor = conn.cursor()

# Create tables
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(15),
    date_of_birth DATE,
    gender CHAR(1)
)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) UNIQUE
)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS professors (
    professor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(15),
    department_id INTEGER REFERENCES departments(department_id)
)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100),
    course_code VARCHAR(10) UNIQUE,
    department_id INTEGER REFERENCES departments(department_id),
    professor_id INTEGER REFERENCES professors(professor_id)
)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(student_id),
    course_id INTEGER REFERENCES courses(course_id),
    enrollment_date DATE,
    UNIQUE(student_id, course_id)
)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS assignments (
    assignment_id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses(course_id),
    assignment_title VARCHAR(100),
    due_date DATE,
    description TEXT
)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS grades (
    grade_id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(student_id),
    assignment_id INTEGER REFERENCES assignments(assignment_id),
    grade CHAR(2),
    feedback TEXT,
    submission_date DATE,
    UNIQUE(student_id, assignment_id)
)
"""
)
conn.commit()

# Insert sample data
cursor.execute(
    """
INSERT INTO departments (department_name)
VALUES
('Computer Science'),
('Mathematics'),
('Physics')
ON CONFLICT (department_name) DO NOTHING
"""
)

cursor.execute(
    """
INSERT INTO professors (first_name, last_name, email, phone_number, department_id)
VALUES
('John', 'Doe', 'john.doe@example.com', '555-1234', 1),
('Jane', 'Smith', 'jane.smith@example.com', '555-5678', 2),
('Albert', 'Einstein', 'albert.einstein@example.com', '555-9101', 3)
ON CONFLICT (email) DO NOTHING
"""
)

cursor.execute(
    """
INSERT INTO courses (course_name, course_code, department_id, professor_id)
VALUES
('Introduction to Computer Science', 'CS101', 1, 1),
('Calculus I', 'MATH101', 2, 2),
('General Physics I', 'PHYS101', 3, 3)
ON CONFLICT (course_code) DO NOTHING
"""
)

cursor.execute(
    """
INSERT INTO students (first_name, last_name, email, phone_number, date_of_birth, gender)
VALUES
('Alice', 'Johnson', 'alice.johnson@example.com', '555-1122', '2000-01-01', 'F'),
('Bob', 'Lee', 'bob.lee@example.com', '555-3344', '1999-02-02', 'M')
ON CONFLICT (email) DO NOTHING
"""
)

cursor.execute(
    """
INSERT INTO enrollments (student_id, course_id, enrollment_date)
VALUES
(1, 1, '2024-07-01'),
(1, 2, '2024-07-01'),
(2, 3, '2024-07-01')
ON CONFLICT (student_id, course_id) DO NOTHING
"""
)

cursor.execute(
    """
INSERT INTO assignments (course_id, assignment_title, due_date, description)
VALUES
(1, 'Assignment 1', '2024-07-10', 'First assignment for CS101'),
(2, 'Assignment 1', '2024-07-10', 'First assignment for MATH101'),
(3, 'Assignment 1', '2024-07-10', 'First assignment for PHYS101')
ON CONFLICT DO NOTHING
"""
)

cursor.execute(
    """
INSERT INTO grades (student_id, assignment_id, grade, feedback, submission_date)
VALUES
(1, 1, 'A', 'Excellent work', '2024-07-09'),
(2, 3, 'B', 'Good effort', '2024-07-09')
ON CONFLICT (student_id, assignment_id) DO NOTHING
"""
)

conn.commit()

# Fetch and display some data
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()
for student in students:
    print(student)

# Close the connection
cursor.close()
conn.close()

