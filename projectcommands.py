import sqlite3

def view_all_projects():
    conn = sqlite3.connect('projectdata.db')
    c = conn.cursor()
    c.execute('''
    SELECT *
    FROM projects''')

    results = list(c.fetchall())

    for index, item in enumerate(results):
        print index, item[0]

    project = int(raw_input("Which project would you like to view? "))
    conn.close()
    return results[project][0]


def add_project():
    conn = sqlite3.connect('projectdata.db')
    c = conn.cursor()
    project_title = raw_input("What is the title of your project? ")
    c.execute('''
    INSERT INTO projects
    (project_title)
    VALUES (?)''',
    (project_title,))

    conn.commit()
    c.close()
    print "Added new project %s to database" % project_title


def view_tasks_in_project(project_title):
    print "Project title is", project_title
    conn = sqlite3.connect('projectdata.db')
    c = conn.cursor()
    c.execute('''
    SELECT *
    FROM tasks
    WHERE project_title=?''',
    (project_title,))

    results = list(c.fetchall())

    for index,item in enumerate(results):
        print index, item[0]

    task_num = int(raw_input("What task would you like to view? "))

    return results[task_num][0]
    conn.close()

    
    
