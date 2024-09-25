import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
import tkinter.font as font

# Function to add task
def add_task():
    task = entry.get()
    if task != "":
        priority = priority_var.get()
        task_deadline = simpledialog.askstring("Task Deadline", "Enter deadline (YYYY-MM-DD):")
        if task_deadline:
            try:
                deadline_date = datetime.strptime(task_deadline, '%Y-%m-%d')
                task = f"{priority}: {task} (Deadline: {task_deadline})"
                task_listbox.insert(tk.END, task)
                entry.delete(0, tk.END)
                check_overdue_tasks()
            except ValueError:
                messagebox.showwarning("Date Error", "Please enter a valid date in YYYY-MM-DD format.")
        else:
            task_listbox.insert(tk.END, task)
            entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to clear all tasks
def clear_tasks():
    task_listbox.delete(0, tk.END)

# Function to edit selected task
def edit_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        current_task = task_listbox.get(selected_task_index)
        new_task = simpledialog.askstring("Edit Task", f"Edit the task:", initialvalue=current_task)
        if new_task:
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, new_task)
            check_overdue_tasks()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")

# Function to mark task as completed
def mark_task_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.itemconfig(selected_task_index, fg="gray")
        task_listbox.selection_clear(selected_task_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Function to search tasks
def search_task():
    query = simpledialog.askstring("Search Task", "Enter keyword to search:")
    if query:
        matching_tasks = []
        for task in task_listbox.get(0, tk.END):
            if query.lower() in task.lower():
                matching_tasks.append(task)
        
        if matching_tasks:
            result = "\n".join(matching_tasks)
            messagebox.showinfo("Search Results", f"Tasks found:\n{result}")
        else:
            messagebox.showinfo("Search Results", "No matching tasks found.")

# Function to check for overdue tasks and highlight them
def check_overdue_tasks():
    for i in range(task_listbox.size()):
        task = task_listbox.get(i)
        if "Deadline:" in task:
            try:
                deadline_str = task.split("Deadline: ")[1].strip(')')
                deadline_date = datetime.strptime(deadline_str, '%Y-%m-%d')
                if deadline_date < datetime.now():
                    task_listbox.itemconfig(i, fg="red")
                else:
                    task_listbox.itemconfig(i, fg="black")
            except ValueError:
                pass

# Function to sort tasks by priority
def sort_tasks():
    tasks = list(task_listbox.get(0, tk.END))
    high_priority = [task for task in tasks if task.startswith("High")]
    medium_priority = [task for task in tasks if task.startswith("Medium")]
    low_priority = [task for task in tasks if task.startswith("Low")]

    task_listbox.delete(0, tk.END)
    for task in high_priority + medium_priority + low_priority:
        task_listbox.insert(tk.END, task)

# Create the main window
root = tk.Tk()
root.title("Enhanced ToDo List App")

# Create the Entry widget for task input
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

# Add priority dropdown
priority_var = tk.StringVar(value="Medium")
priority_menu = tk.OptionMenu(root, priority_var, "High", "Medium", "Low")
priority_menu.grid(row=0, column=1, padx=10, pady=10)

# Add task button
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.grid(row=0, column=2, padx=10, pady=10)

# Create the Listbox to display tasks
task_listbox = tk.Listbox(root, height=10, width=60)
task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Add Scrollbar to the Listbox
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=1, column=3, sticky='ns')
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Delete task button
delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.grid(row=2, column=0, padx=10, pady=10)

# Clear tasks button
clear_button = tk.Button(root, text="Clear All", width=20, command=clear_tasks)
clear_button.grid(row=2, column=1, padx=10, pady=10)

# Mark task as completed button
mark_button = tk.Button(root, text="Mark Completed", width=20, command=mark_task_completed)
mark_button.grid(row=2, column=2, padx=10, pady=10)

# Edit task button
edit_button = tk.Button(root, text="Edit Task", width=20, command=edit_task)
edit_button.grid(row=3, column=0, padx=10, pady=10)

# Sort tasks button
sort_button = tk.Button(root, text="Sort Tasks by Priority", width=20, command=sort_tasks)
sort_button.grid(row=3, column=1, padx=10, pady=10)

# Search task button
search_button = tk.Button(root, text="Search Task", width=20, command=search_task)
search_button.grid(row=3, column=2, padx=10, pady=10)

# Run the application
root.mainloop()
