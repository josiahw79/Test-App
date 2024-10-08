import tkinter as tk
from tkinter import messagebox

def show_popup():
    messagebox.showinfo("Hello", "If you can see this that means I did my big one")

window=tk.Tk()
window.title("Hello")

greeting=tk.Label(text="Hello, if you can see this that means that the code is working 😆")
greeting.pack()


button=tk.Button(
    window,
    text="Click Me",
    bg="gray",
    fg="black",
    command=show_popup)

button.pack()

window.mainloop()