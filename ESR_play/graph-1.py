import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import *

import subprocess
import webbrowser
import sys

import graph1  # import the graph1 module


def import_csv_data():
    global v
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    df = pd.read_csv(csv_file_path)

# Define the functions before calling them


def doNothing():
    print("nothing")


def create_window():
    window = tk.Tk()

# Define a function for 'Graph 1' button. This just calls the 'display_graph' function from
# the 'graph1' module.
# You could avoid defining this function and use lambda and graph1.display_graph(v.get())
# in the 'Graph 1' button command but I prefer it this way.


def graph_1():
    graph1.display_graph(v.get())


root = tk.Tk()
tk.Label(root, text='File Path').grid(row=0, column=0)
v = tk.StringVar()
entry = tk.Entry(root, textvariable=v).grid(row=0, column=1)
tk.Button(root, text='Browse Data Set',
          command=import_csv_data).grid(row=1, column=0)
tk.Button(root, text='Close', command=root.destroy).grid(row=1, column=1)

tk.Button(root, text='Graph', command=graph_1).grid(
    row=3, column=0)  # Call the graph_1 function


menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New", command=doNothing)
subMenu.add_command(label="Open", command=doNothing)
subMenu.add_command(label="Restart", command=doNothing)
subMenu.add_command(label="Exit", command=doNothing)
editMenu = Menu(menu)
menu.add_cascade(label="Help", menu=editMenu)
editMenu.add_command(label="Help", command=doNothing)

root.mainloop()
