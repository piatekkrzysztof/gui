from tkinter import *
import json

# clicks = 0
#
#
# def click_action(button):
#     global clicks
#     clicks += 1
#     button.config(text=f"Wow! x {clicks}")
#
#
# # def create_command(func, *args, **kwargs):  // or lambda
# #     def command():
# #         return func(*args, **kwargs)
# #     return command
#
#
# root = Tk()
#
# root.title("App")
# root.geometry("200x200")
#
# label = Label(root, text='look at me', font=30, fg='blue')
# label.pack()
#
# click_button = Button(root,text='Click me', width=8)
# click_button.pack()
#
# click_button.config(command=lambda: click_action(click_button))
#
#
#
#
# root.mainloop()

def add_task():
    task=task_entry.get()
    if task:
        task_listbox.insert(END, task)
        task_entry.delete(0, END)


def delete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except IndexError:
        pass


def save_tasks():
    tasks=task_listbox.get(0, END)
    with open('tasks.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)


def load_tasks():
    try:
        with open('tasks.json', 'r', encoding='utf-8') as f:
            tasks = json.load(f)
            for task in tasks:
                task_listbox.insert(END, task)
    except FileNotFoundError:
        pass


def on_closing():
    save_tasks()
    root.destroy()


root = Tk()
root.title("U To Do")
root.protocol("WM_DELETE_WINDOW", on_closing)

task_entry = Entry(root, width=50, )
task_entry.pack(pady=10)

add_button = Button(root, text="Add Task", command=add_task)
add_button.pack()

task_listbox = Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

load_tasks()

delete_button = Button(root, text="Delete", command=delete_task)
delete_button.pack()

root.mainloop()
