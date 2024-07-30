# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 23:39:11 2024

@author: ryand
"""

class Task:
    def __init__(self, task_id, title, description):
        self.id = task_id
        self.title = title
        self.description = description

    def __str__(self):
        return f"Task(id = {self.id}, title = {self.title}, description = {self.description})"

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def create_task(self, title, description):
        task = Task(self.next_id, title, description)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def edit_task(self, task_id, new_title, new_description):
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task.title = new_title
            task.description = new_description
            return task
        else:
            raise ValueError("Task ID does not exist")

    def delete_task(self, task_id):
        print("Are you sure you want to delete? All reminders and information will be lost.")
        choice = input("Yes - 1 / No - 2: ")
        
        if choice == '1':
            if task_id in self.tasks:
                del self.tasks[task_id]
            else:
                raise ValueError("Task ID does not exist")

    def list_tasks(self):
        return list(self.tasks.values())

def main():
    task_manager = TaskManager()
    while True:
        print("\nTask Management\n-----------------------------------------------------------------------------")
        print("\ 1. Create Task \ 2. Edit Task \ 3. Delete Task \ 4. List Tasks \ 5. Exit\n-----------------------------------------------------------------------------")
        tasks = task_manager.list_tasks()
        if tasks:
            for task in tasks:
                print(str(task.id) + " - " + task.title)
        else:
            print("No tasks found")
        print("\ Create tasks to organize projects, have a plan for the future, stoy on\n\ task with reminders, share tasks with groups, and be more productive")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = task_manager.create_task(title, description)
            print(f"Task created: {task}")
        elif choice == '2':
            task_id = int(input("Enter task ID to edit: "))
            new_title = input("Enter new task title: ")
            new_description = input("Enter new task description: ")
            try:
                task = task_manager.edit_task(task_id, new_title, new_description)
                print(f"Task updated: {task}")
            except ValueError as e:
                print(e)
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            try:
                task_manager.delete_task(task_id)
                print("Task deleted")
            except ValueError as e:
                print(e)
        elif choice == '4':
            tasks = task_manager.list_tasks()
            if tasks:
                for task in tasks:
                    print(task)
            else:
                print("No tasks found")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
