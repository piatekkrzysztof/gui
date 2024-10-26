from tkinter import Tk, Label, Button

clicks = 0


def click_action(button):
    global clicks
    clicks += 1
    button.config(text=f"Wow! x {clicks}")
    

# def create_command(func, *args, **kwargs):  // or lambda
#     def command():
#         return func(*args, **kwargs)
#     return command


root = Tk()

root.title("App")
root.geometry("200x200")

label = Label(root, text='look at me', font=30, fg='blue')
label.pack()

click_button = Button(root,text='Click me', width=8)
click_button.pack()

click_button.config(command=lambda: click_action(click_button))




root.mainloop()
