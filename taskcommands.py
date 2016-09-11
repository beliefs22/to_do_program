import sqlite3


def add_task(project_title):
    task_title = raw_input("What is the title of your task? ")
    start_date= raw_input("What is the start date for your task? ")
    due_date = raw_input("What is the due_date for your task? ")
    notes = raw_input("What notes would you like to make? ")
    status = raw_input("What is the initial status of your task ")
    conn = sqlite3.connect('projectdata.db')
    c = conn.cursor()
    c.execute('''
    INSERT INTO tasks
    (task_title, project_title, start_date, due_date, notes, status)
    VALUES (?,?,?,?,?,?)''',
    (task_title, project_title, start_date, due_date, notes, status))
    conn.commit()
    c.close()

def view_notes(task_title, project_title):
    conn = sqlite3.connect('projectdata.db')
    c = conn.cursor()

    c.execute('''
    SELECT notes
    FROM tasks
    WHERE task_title=? AND project_title=?''',
    (task_title, project_title))

    results = c.fetchone()[0]

    print "Current notes are %s" % results
    

def update_due_date(task_title,project_title):
    conn = sqlite3.connect('projectdata.db')
    c = conn.cursor()
    
    c.execute('''
    SELECT due_date
    FROM tasks
    WHERE task_title=? AND project_title=?''',
    (task_title,project_title))

    current_date = c.fetchone()[0]
    print "Current status is %s" % current_date

    new_date = raw_input("What to change status to? ")

    c.execute('''
    UPDATE tasks
    SET due_date=?
    WHERE task_title=? AND project_title=?''',
    (new_date, task_title, project_title))
    conn.commit()
    conn.close()

def update_status(task_title, project_title):
    conn = sqlite3.connect('projectdata.db')
    c = conn.cursor()
    
    c.execute('''
    SELECT status
    FROM tasks
    WHERE task_title=? AND project_title=?''',
    (task_title,project_title))

    current_status = c.fetchone()[0]
    print "Current status is %s" % current_status

    new_status = raw_input("What to change status to? ")

    c.execute('''
    UPDATE tasks
    SET status=?
    WHERE task_title=? AND project_title=?''',
    (new_status, task_title, project_title))
    conn.commit()
    conn.close()

def update_notes(task_title, project_title):
    conn = sqlite3.connect('projectdata.db')
    c = conn.cursor()
    
    c.execute('''
    SELECT notes
    FROM tasks
    WHERE task_title=? AND project_title=?''',
    (task_title,project_title))

    current_notes = c.fetchone()[0]
    print "Current status is %s" % current_notes

    new_notes = raw_input("What to change status to? ")
    new_notes = current_notes + "," + new_notes

    c.execute('''
    UPDATE tasks
    SET notes=?
    WHERE task_title=? AND project_title=?''',
    (new_notes, task_title, project_title))

    conn.commit()
    conn.close()

def show_all_pending_task():
    conn = sqlite3.connect('projectdata.db')
    c = conn.cursor()

    c.execute('''
    SELECT *
    FROM tasks''')

    results =  list(c.fetchall())
    for task in results:
        print """
        Task: %s
        Project: %s
        Start Date: %s
        Due Date: %s
        Notes: %s
        Status: %s
        _______________________________________________________________
        
        """ % task
    conn.close()
    
    

