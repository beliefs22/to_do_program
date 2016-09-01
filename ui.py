def inital_options():
    print " 1. View all Projects"
    print " 2. Add Project"
    print " 3. View Task Due this Week"
    print " 4. View Task Due this Month"
    print " 5. View Critical Task"

    ans = raw_input("Please Choose an option")
    return ans

def project_options():
    print " 1. View Incomplete Tasks"
    print " 2. View Complete Tasks"
    print " 3. Add task to project"
    print " 4. Update task"
    print " 5. View All tasks"

    ans = raw_input("Please Choose an option")
    return ans

def get_project_info():
    return raw_input("What is the title of your project?")

def task_options():
    print " 1. View Notes"
    print " 2. Update Status"
    print " 3. Update Notes"
    print " 4. Update Due Date"

    ans = raw_input("Please Choose an option")
    return ans


