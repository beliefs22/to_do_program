import sqlite3
import projectcommands as project
import taskcommands as task

def initial_options():
    print " 1. Select a current Projects"
    print " 2. Add Project"
    print " 3. View Task Due this Week"
    print " 4. View Task Due this Month"
    print " 5. View Critical Task"
    print " 6. Quit "

    ans = raw_input("Please Choose an option ")
    return ans

def project_options():
    print " 1. View Incomplete Tasks"
    print " 2. View Complete Tasks"
    print " 3. Add task to project"
    print " 4. Update task"
    print " 5. View All tasks"
    print " 6. Quit "
    ans = raw_input("Please Choose an option ")
    return ans

def task_options():
    print " 1. View Notes"
    print " 2. Update Status"
    print " 3. Update Notes"
    print " 4. Update Due Date"
    print " 5. Quit "
    ans = raw_input("Please Choose an option ")
    return ans


def main():
    while True:
        choice = initial_options()

        if choice == "1":
            project_title = project.view_all_projects()
            while True:
                choice2 = project_options()
                if choice2 == "6":
                    break
                if choice2 == "5":
                    task_title = project.view_tasks_in_project(project_title)
                    while True:
                        choice3 = task_options()
                        if choice3 == "5":
                            break
                        if choice3 == "2":
                            task.update_status(task_title, project_title)
                        if choice3 == "3":
                            task.update_notes(task_title, project_title)
                        if choice3 == "4":
                            task.update_due_date(task_title,project_title)
                        if choice3 == "1":
                            task.view_notes(task_title, project_title)
                            
                if choice2 == "3":
                    task.add_task(project_title)
                    
        if choice == "2":
            project.add_project()

        if choice == "6":
            break
if __name__ == "__main__":
    main()
        
