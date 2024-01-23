import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task = listbox.curselection()
        listbox.delete(selected_task)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

root.configure(bg="black")

entry = tk.Entry(root, width=40, bg="white", fg="black") 
entry.pack(pady=20)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#59CE8F", fg="black") 
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#59CE8F", fg="black")  
delete_button.pack(pady=5)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10, bg="white", fg="black")  
listbox.pack(pady=10)

root.mainloop()
