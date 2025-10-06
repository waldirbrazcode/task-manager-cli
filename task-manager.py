import json
import datetime
import os

print("Welcome to task manager!")

def add(tasks):
    nametask = input("Add a name for the task: ")
    desctask = input("Add a description for the task: ")
    creationdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    task = {
        "order": len(tasks) + 1,
        "id": len(tasks) + 1,
        "nametask": nametask,
        "desctask": desctask,
        "creationdate": creationdate,
        "status": "To-do"
    }

    tasks.append(task)

    with open("task-data.json", "w", encoding="utf-8") as a:
        json.dump(tasks, a, indent=4, ensure_ascii=False)

    main()

def loadtasks():
    if not os.path.exists('task-data.json'):
        return []
    
    with open('task-data.json', 'r', encoding='utf-8') as a:
        return json.load(a)
    
def see_all(tasks):
    if not tasks:
        print("Not tasks created yet")
        main()
    
    for task in tasks:
        print(f"{task["order"]} - {task["nametask"]}: {task["desctask"]}\nId: {task["id"]}\nStatus: {task["status"]}\nCreated at: {task["creationdate"]}\n")
    
    main()

def delete(tasks):
    idtask = int(input("Insert the id of the task: "))

    if idtask > len(tasks) or idtask < 0:
        print("Invalid number id")
        main()

    for task in tasks:
        if task["id"] == idtask:
            tasks.remove(task)

    for order, task in enumerate(tasks, start=1):
        task.update({"order": order})

    with open('task-data.json', 'w') as a:
        json.dump(tasks, a, indent=4)

    main()

def deleteall(tasks):
    tasks.clear()

    with open("task-data.json", "w") as a:
        json.dump(tasks, a, indent=4)

    main()

def update(tasks):
    idtask = int(input("Insert the id of the task: "))
    idtask -= 1

    if idtask > len(tasks) or idtask < 0:
        print("Invalid number id")
        main()

    statusupdate = int(input("0: To-do\n1: Done\n"))

    if statusupdate == 0:
        tasks[idtask].update({"status": "To-do"})
    elif statusupdate == 1:
        tasks[idtask].update({"status": "Done"})
    else:
        print("Insert a valid number")
        main()

    with open("task-data.json", "w") as a:
        json.dump(tasks, a, indent=4)

    main()

def main():
    tasks = loadtasks()
    print("\nCommands:")
    print("add\nupdate\ndelete\ndelete-all\nsee-all\nsee-done\nsee-todo\nexit\n")

    command = input()

    match command:
        case "add":
            add(tasks)

        case "see-all":
            see_all(tasks)

        case "delete":
            delete(tasks)

        case "delete-all":
            deleteall(tasks)

        case "update":
            update(tasks)

if __name__ == '__main__':
    main()