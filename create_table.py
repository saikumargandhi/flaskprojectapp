import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE projects (project_name TEXT, project_tools TEXT, project_desc TEXT)')
print("Table created successfully")
conn.close()