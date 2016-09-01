import sqlite3

conn = sqlite3.connect('projectdata.db')

c = conn.cursor()

def add_project(project_title):
    c.execute('''
    INSERT INTO projects
    (project_title)
    VALUES (?)''',
    (project_title))

    conn.commit()
    c.close()

def add_task(task_title,project_title,start_date,
             due_date=None, notes=None,status=None):
    c.execute('''
    INSERT INTO tasks
    (task_title, project_title, start_date, due_date, notes, status)
    VALUES (?,?,?,?,?,?)''',
    (task_title, project_title, start_date, due_date, notes, status))

    conn.commit()
    c.close()

def update_task(name,project,status=None,due=None,notes=None):
    c.execute('''
    UPDATE tasks
    SET status=?, due_date=?, notes=?
    WHERE task_title =? AND project_title=?''',
    (status,due,notes,name,project))

    conn.commit()
    c.close()
def view_projects(timeframe):
    pass
