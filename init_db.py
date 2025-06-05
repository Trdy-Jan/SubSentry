import sqlite3

conn = sqlite3.connect('tasks.db')
c = conn.cursor()
c.execute('''
          CREATE TABLE IF NOT EXISTS tasks (
                                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                                               user_id INTEGER NOT NULL,
                                               service_name TEXT NOT NULL,
                                               due_date TEXT NOT NULL,
                                               remind_days INTEGER DEFAULT 3,
                                               repeat_days INTEGER DEFAULT NULL,
                                               persistent_reminder INTEGER DEFAULT 0
          )
          ''')
conn.commit()
conn.close()
print("Database initialized.")
