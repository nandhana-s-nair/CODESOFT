import tkinter as tk
from tkinter import messagebox

tasks = []

def refresh_tasks():
    task_list.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["done"] else "✗"
        task_list.insert(tk.END, f"{status}  {task['title']}")

def add_task():
    task = task_entry.get()
    if task.strip() == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return
    tasks.append({"title": task, "done": False})
    task_entry.delete(0, tk.END)
    refresh_tasks()

def delete_task():
    try:
        index = task_list.curselection()[0]
        tasks.pop(index)
        refresh_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task first!")

def complete_task():
    try:
        index = task_list.curselection()[0]
        tasks[index]["done"] = True
        refresh_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task first!")

# ------------------- GUI -------------------

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x450")
root.configure(bg="#e6f2ff")

# Title
title = tk.Label(root, text="📝 TO-DO LIST", font=("Helvetica", 20, "bold"), bg="#e6f2ff")
title.grid(row=0, column=0, columnspan=3, pady=15)

# Entry + Add Button Row
task_entry = tk.Entry(root, font=("Arial", 12), width=30)
task_entry.grid(row=1, column=0, padx=10, pady=10)

add_btn = tk.Button(root, text="Add", width=12, command=add_task)
add_btn.grid(row=1, column=1, padx=5)

# Task List Area
task_frame = tk.Frame(root)
task_frame.grid(row=2, column=0, columnspan=3, pady=10)

scrollbar = tk.Scrollbar(task_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_list = tk.Listbox(
    task_frame,
    width=55,
    height=15,
    font=("Arial", 11),
    yscrollcommand=scrollbar.set
)
task_list.pack()

scrollbar.config(command=task_list.yview)

# Bottom Buttons
complete_btn = tk.Button(root, text="Mark Complete", width=15, command=complete_task)
complete_btn.grid(row=3, column=0, pady=15)

delete_btn = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_btn.grid(row=3, column=1)

exit_btn = tk.Button(root, text="Exit", width=15, command=root.quit)
exit_btn.grid(row=3, column=2)

root.mainloop()