import os
import datetime

def validate_user(username, password):
    with open('user.txt', 'r') as file:
        for line in file:
            user, pwd = line.strip().split(', ')
            if user == username and pwd == password:
                return True
    return False

def register_user():
    if username != 'admin':
        print("Only admin can register new users.")
        return
    new_username = input("Enter new username: ")
    new_password = input("Enter new password: ")
    confirm_password = input("Confirm password: ")
    if new_password == confirm_password:
        with open('user.txt', 'a') as file:
            file.write(f"\n{new_username}, {new_password}")
        print("User registered successfully.")
    else:
        print("Passwords do not match. User registration failed.")

def add_task():
    assigned_user = input("Enter the username of the person the task is assigned to: ")
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter the description of the task: ")
    due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    with open('tasks.txt', 'a') as file:
        file.write(f"\n{assigned_user}, {task_title}, {task_description}, {current_date}, {due_date}, No")
    print("Task added successfully.")

def view_all_tasks():
    with open('tasks.txt', 'r') as file:
        for line in file:
            print(line.strip())

def view_my_tasks(username):
    with open('tasks.txt', 'r') as file:
        for line in file:
            task_info = line.strip().split(', ')
            if task_info[0] == username:
                print(', '.join(task_info))

def display_statistics(username):
    if username != 'admin':
        print("Only admin can view statistics.")
        return
    total_users = sum(1 for line in open('user.txt'))
    total_tasks = sum(1 for line in open('tasks.txt'))
    print(f"Total number of users: {total_users}")
    print(f"Total number of tasks: {total_tasks}")

while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if validate_user(username, password):
        while True:
            menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - display statistics
e - exit
: ''').lower()
            if menu == 'r':
                register_user()
            elif menu == 'a':
                add_task()
            elif menu == 'va':
                view_all_tasks()
            elif menu == 'vm':
                view_my_tasks(username)
            elif menu == 's':
                display_statistics(username)
            elif menu == 'e':
                print('Goodbye!')
                exit()
            else:
                print("You have entered an invalid input. Please try again")
    else:
        print("Invalid username or password. Please try again")
