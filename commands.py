import sqlite3

def add_project(project_title):
    conn = sqlite3.connect('projectdata.db')
    c = conn.cursor()
    c.execute('''
    INSERT INTO projects
    (project_title)
    VALUES (?)''',
    (project_title))

    conn.commit()
    c.close()

def add_task(task_title,project_title,start_date,
             due_date=None, notes=None,status=None):
    conn = sqlite3.connect('projectdata.db')
    c = conn.cursor()
    c.execute('''
    INSERT INTO tasks
    (task_title, project_title, start_date, due_date, notes, status)
    VALUES (?,?,?,?,?,?)''',
    (task_title, project_title, start_date, due_date, notes, status))

    conn.commit()
    c.close()

def update_task(task_title,project_title,status=None,due_date=None,notes=None):
    conn = sqlite3.connect('projectdata.db')
    c = conn.cursor()
    c.execute('''
    UPDATE tasks
    SET status=?, due_date=?, notes=?
    WHERE task_title =? AND project_title=?''',
    (status,due_date,notes,task_title,project_title))

    conn.commit()
    c.close()
def view_projects(timeframe):
    pass
