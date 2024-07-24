# Create an employee management system to manage employees with the following functionalities:
# Add new employees with name, position, and salary.
# Update an employee's position and salary.
# Delete an employee.
# View all employees.

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Create employees table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    position TEXT,
    salary REAL
)
"""
)
conn.commit()


# Add a new employee
def add_employee(name, position, salary):
    cursor.execute(
        """
    INSERT INTO employees (name, position, salary)
    VALUES (?, ?, ?)
    """,
        (name, position, salary),
    )
    conn.commit()


# Update an employee's position and salary
def update_employee(employee_id, position, salary):
    cursor.execute(
        """
    UPDATE employees
    SET position = ?, salary = ?
    WHERE id = ?
    """,
        (position, salary, employee_id),
    )
    conn.commit()


# Delete an employee
def delete_employee(employee_id):
    cursor.execute(
        """
    DELETE FROM employees
    WHERE id = ?
    """,
        (employee_id,),
    )
    conn.commit()


# View all employees
def view_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    for employee in employees:
        print(employee)


add_employee("John Doe", "Software Engineer", 60000)
add_employee("Jane Smith", "Project Manager", 80000)
update_employee(1, "Senior Software Engineer", 75000)
delete_employee(2)
view_employees()

# Close the connection
conn.close()
