import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("After demo")

my_label = tk.Label(root, text="This is place holder label")
my_label.grid(column=0, row=0)


def show_time():
    curtime = datetime().time()
    msg = "The current this is ()" .format(curtime)
    my_label.configure(text=msg)
    root.after(2000, show_time)


root.after(2000, show_time)
root.mainloop()
