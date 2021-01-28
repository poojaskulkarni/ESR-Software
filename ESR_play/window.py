import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import esr_funcs


global df
global par
df = [[0 for i in range(100)] for j in range(10)]  # register data

# parameters (similar to old code)
# Par[Rn,0] = Size
#Par[Rn,1] = Ic
#Par[Rn,2] = 13.09/(Ic2-Ic)
#Par[Rn,3] = Ss
#Par[Rn,4] = N1
#Par[Rn,5] = N2
par = [[0 for i in range(6)] for j in range(10)]


def replot():

    figure = plt.Figure(figsize=(5, 4), dpi=100)
    ax = figure.add_subplot(111)
    labels = []
    for i in range(10):
        if(graph_reg[i].get()):
            ax.plot(range(len(df[i])), df[i])
            labels.append('Reg' + str(i))

    plot1 = FigureCanvasTkAgg(figure, window)
    plot1.get_tk_widget().grid(row=0, column=7, rowspan=20)
    ax.legend(labels)
    ax.set_xlabel('Magnetic Field (T)')
    ax.set_title('Magnetic Field Vs. ESR')


def import_txt_data(reg_num):
    global reg_string

    txt_file_path = askopenfilename()

    reg_string[reg_num].set(txt_file_path)
    global df

    df[reg_num] = pd.read_csv(txt_file_path, names=[
        'ESR Values'], skiprows=4, skipfooter=16).to_numpy()

    print(df[reg_num])
    replot()


def baselineButton(reg_num):
    df[reg_num] = esr_funcs.baseline(df[reg_num])
    replot()


def findButton(reg_num):
    par[reg_num][4], par[reg_num][5] = esr_funcs.find(df[reg_num])
    replot()


def refindButton(reg_num):
    par[reg_num][4], par[reg_num][5] = (0, par[reg_num][0])
    replot()


def integrateButton(reg_num):
    par[reg_num][3] = esr_funcs.integrate(df[reg_num])
    replot()


window = tk.Tk()


global graph_check
global reg_string

graph_reg = []
for i in range(10):
    graph_reg.append(IntVar())

reg_string = []
for i in range(10):
    reg_string.append(tk.StringVar())


#
#
#
#
# CREATE WINDOW
#
#
#
#


label0 = tk.Label(text="Register 0:")
label0.grid(row=0, column=0)
entry0 = tk.Entry(window, textvariable=reg_string[0]).grid(
    row=0, column=1, columnspan=5)
tk.Button(window, text='Browse Data Set',
          command=lambda: import_txt_data(0)).grid(row=1, column=0)
tk.Checkbutton(window, text='Graph',
               command=replot, variable=graph_reg[0]).grid(row=1, column=1)
tk.Button(window, text='Baseline',
          command=lambda: baselineButton(0)).grid(row=1, column=2)
tk.Button(window, text='Find',
          command=lambda: findButton(0)).grid(row=1, column=3)
tk.Button(window, text='Refind',
          command=lambda: refindButton(0)).grid(row=1, column=4)
tk.Button(window, text='Integrate',
          command=lambda: integrateButton(0)).grid(row=1, column=5)
tk.Label(window, text='Double Integral:').grid(row=1, column=6)


label1 = tk.Label(text="Register 1:")
label1.grid(row=2, column=0)
entry1 = tk.Entry(window, textvariable=reg_string[1]).grid(
    row=2, column=1, columnspan=5)
tk.Button(window, text='Browse Data Set',
          command=lambda: import_txt_data(1)).grid(row=3, column=0)
tk.Checkbutton(window, text='Graph',
               command=replot, variable=graph_reg[1]).grid(row=3, column=1)
tk.Button(window, text='Baseline',
          command=lambda: baselineButton(1)).grid(row=3, column=2)
tk.Button(window, text='Find',
          command=lambda: findButton(1)).grid(row=3, column=3)
tk.Button(window, text='Refind',
          command=lambda: refindButton(1)).grid(row=3, column=4)
tk.Button(window, text='Integrate',
          command=lambda: integrateButton(1)).grid(row=3, column=5)
tk.Label(window, text='Double Integral:').grid(row=3, column=6)


replot()


window.mainloop()
