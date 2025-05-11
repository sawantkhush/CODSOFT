import os
import json

tasks_file = "tasks.json"

# load tasks from the file, if file dosen't exists return empty list(view tasks)
def load_tasks():
    if os.path.exists(tasks_file):
        with open(tasks_file, 'r') as f:
            return json.load(f)
    return []

# add tasks, by the user
def add_task(tasks):
        print("Enter your tasks one by one. Type 'done' when you're finished.\n")
        while True:
            title = input(f"Task {len(tasks) + 1}: ").strip() 
            if title == "done":
                print("Tasks added")
                break
            elif title:
                
#for the view tasks purpose that is each and every task is added to the list of the tasks
                tasks.append({"title": title, "done": False})
            else:
                print("Empty task ignored.")
              
# display tasks with status (entirely)
def status_task(tasks):
    if not tasks:
        print("No tasks yet")
        return    
# For each task, show its number, title, and status
    for i, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "Not done"
        print(f"{i}. {task['title']} [{status}]")
      

       
# mark a selected task as completed
def mark_done(tasks):
    status_task(tasks)
    index_task = int(input("Enter task number to be completed :")) -1
    if 0 <= index_task <len(tasks):
        tasks[index_task]["done"] = True
        print("Task marked as done")
    else :
        print("Invalid task number")

#delete a task
def delete_task(tasks):
     status_task(tasks)#show current tasks/all tasks
     index_task = int(input("Enter task number to be deleted : ")) -1
     if 0 <= index_task < len(tasks):
         deleted = tasks.pop(index_task)
         print(f"Task deleted : {deleted['title']}")
     else :
         print("Invalid task number")

#main menu
def menu():
    tasks = load_tasks()
    while True:
        print("\nTo-Do list Menu:")
        print("1. View tasks")
        print("2. Add tasks")
        print("3. Mark task as completed")
        print("4. Delete tasks")
        print("5. Exit")

#use match case for handling the user input
        choice = input("Enter your choice:")
        match choice:
            case '1':
                status_task(tasks)
            case '2':
                add_task(tasks)
            case '3':
                mark_done(tasks)
            case '4':
                delete_task(tasks)
            case '5':
                print("Tasks updated")
                break
            case _:
                print("Invalid number")
            
             #run the app
if __name__ == "__main__":
              menu()










        
