"""
Intership Task - Python Programming

Task: Build a Command Line To-Do List Application

Description:
This Python program is a simple command line to-do list application.
It allows users to manage their daily tasks by providing the following features:
1. Add a new task
2. View Current tasks
3. Mark a task as completed
4. Delete a task

The code is written using Object-Oriented Programming (OOP) principles and does not use any external libraries.

Samarth Bhawsar
"""

class Task:
    def __init__(self, name):
        self.name = name
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "✓" if self.done else "✗"
        return f"[{status}] {self.name}"
    
class ToDoList:
    def __init__(self):
        self.tasks = []

    def show_tasks(self):
        if not self.tasks:
            print("No tasks added yet\n")
            return 
        print("Current Tasks\n")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")
        print()

    def add_task(self):
        name = input("Enter a task to add:").strip()
        if name:
            self.tasks.append(Task(name))
            print("Task added!\n")
        else:
            print("Task cannot be empty!\n")

    def complete_task(self):
        self.show_tasks()
        if not self.tasks:
            return 
        try:
            num = int(input("Which task number is completed?")) - 1
            if 0 <= num < len(self.tasks):
                self.tasks[num].mark_done()
                print("Marked as Done!\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number!\n")

    def delete_task(self):
        self.show_tasks()
        if not self.tasks:
            return
        try:
            num = int(input("Enter the task number to delete:")) - 1
            if 0 <= num < len(self.tasks):
                remove = self.tasks.pop(num)
                print(f"Deleted Task: {remove.name}\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Enter a valid number!\n")

    def start(self):
        while True:
            print("TO-DO MENU")
            print("1. Show Tasks")
            print("2. Add Task")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Exit")
            choice = input("Enter your choice:").strip()

            if choice == '1':
                self.show_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.complete_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                print("Exiting...Have a great Day!")
                break
            else:
                print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    app = ToDoList()
    app.start()