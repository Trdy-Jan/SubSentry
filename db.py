import sqlite3
from datetime import datetime, timedelta

def get_conn():
    return sqlite3.connect('tasks.db')

def add_task(user_id, service, due_date):
    with get_conn() as conn:
        conn.execute(
            "INSERT INTO tasks (user_id, service_name, due_date) VALUES (?, ?, ?)",
            (user_id, service, due_date)
        )

def list_tasks(user_id):
    with get_conn() as conn:
        cur = conn.execute("SELECT * FROM tasks WHERE user_id=?", (user_id,))
        return cur.fetchall()

def delete_task(task_id):
    with get_conn() as conn:
        conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))

def edit_task(task_id, field, value):
    with get_conn() as conn:
        try:
            conn.execute(f"UPDATE tasks SET {field} = ? WHERE id = ?", (value, task_id))
            return True
        except:
            return False

def get_tasks_due_in_days(days):
    target_date = (datetime.today() + timedelta(days=days)).strftime('%Y-%m-%d')
    with get_conn() as conn:
        cur = conn.execute("SELECT * FROM tasks WHERE due_date=?", (target_date,))
        return cur.fetchall()

def get_persistent_tasks(today):
    with get_conn() as conn:
        cur = conn.execute("SELECT * FROM tasks WHERE persistent_reminder = 1 AND due_date >= ?", (today,))
        return cur.fetchall()

def get_repeat_tasks(today):
    with get_conn() as conn:
        cur = conn.execute("SELECT * FROM tasks WHERE repeat_days IS NOT NULL AND due_date = ?", (today,))
        return cur.fetchall()

def update_repeat_task(task_id, new_date):
    with get_conn() as conn:
        conn.execute("UPDATE tasks SET due_date = ? WHERE id = ?", (new_date, task_id))
