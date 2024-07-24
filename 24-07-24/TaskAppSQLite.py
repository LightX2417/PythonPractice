# Create a task management application to manage tasks with the following functionalities:
# Add a new task with a title, description, and status (e.g., 'Pending', 'Completed').
# Update the status of a task.
# Delete a task.
# View all tasks.

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Create tasks table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    status TEXT
)
"""
)
conn.commit()


# Add a new task
def add_task(title, description, status="Pending"):
    cursor.execute(
        """
    INSERT INTO tasks (title, description, status)
    VALUES (?, ?, ?)
    """,
        (title, description, status),
    )
    conn.commit()


# Update the status of a task
def update_task_status(task_id, status):
    cursor.execute(
        """
    UPDATE tasks
    SET status = ?
    WHERE id = ?
    """,
        (status, task_id),
    )
    conn.commit()


# Delete a task
def delete_task(task_id):
    cursor.execute(
        """
    DELETE FROM tasks
    WHERE id = ?
    """,
        (task_id,),
    )
    conn.commit()


# View all tasks
def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)


add_task("Buy groceries", "Buy milk, eggs, and bread")
add_task("Clean the house", "Clean the living room and kitchen")
update_task_status(1, "Completed")
delete_task(2)
view_tasks()

# Close the connection
conn.close()
