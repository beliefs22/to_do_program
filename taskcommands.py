def get_task_initial_info():
    task_title = raw_input("What is the title of your task? ")
    start_date= raw_input("What is the starte date for your task? ")
    due_date = raw_input("What is the due_date for your task? ")
    notes = raw_input("What notes would you like to make? ")
    status = raw_input("What is the initial status of your task ")
    return task_title, start_date, due_date, notes, status

def update_status(task_title, project_title):
    conn = sqlite3.connect('projectdata.db')
    c = conn.cursor()

    c.execute('''
    SELECT
