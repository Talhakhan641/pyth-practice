from task import Task
import json

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    def save_tasks(self):
        data = []
        for task in self.tasks:
            data.append(task.to_dict())
        with open("tasks.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                data = json.load(file)

            for item in data:
                task = Task(
                    item["id"],
                    item["title"],
                    item["done"]
                )
                self.tasks.append(task)

            if self.tasks:
                self.next_id = max(task.task_id for task in self.tasks) + 1

        except FileNotFoundError:
            print("No saved tasks found. Starting with an empty list.")

    

    def add_task(self, title):
        task = Task(self.next_id, title, False)
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        print(f"Task '{title}' added successfully.")
        

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.done = True
                self.save_tasks()
                print(f"Task {task_id} marked as done.")
                return
        print(f"Task {task_id} not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"Task {task_id} deleted.")
                return
        print(f"Task {task_id} not found.")
    
          

    
    