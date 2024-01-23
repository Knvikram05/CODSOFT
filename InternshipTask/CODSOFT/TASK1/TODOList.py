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

# Set specific colors
bg_color = "#22A699"   # Background color
entry_bg_color = "#F8FAE5"  # Entry box background color
button_bg_color = "#F24C3D"  # Button background color

root.configure(bg=bg_color)

add_button = tk.Button(root, text="Add Task", command=add_task, bg=button_bg_color, fg="white") 
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg=button_bg_color, fg="white")  
delete_button.pack(pady=5)

entry = tk.Entry(root, width=40, bg=entry_bg_color, fg="black") 
entry.pack(pady=20)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10, bg="white", fg="black")  
listbox.pack(pady=10)

root.mainloop()
