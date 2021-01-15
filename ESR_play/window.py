import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def replot():

    figure = plt.Figure(figsize=(5, 4), dpi=100)
    ax = figure.add_subplot(111)
    labels = ''
    if(i1.get()):
        ax.plot(df1['Magnetic Field Values'], df1['ESR Values'], color='g')
        labels = [labels, 'Reg 1']
    if(i2.get()):
        ax.plot(df2['Magnetic Field Values'], df2['ESR Values'], color='b')
        labels = [labels, 'Reg 2']
    if(i3.get()):
        ax.plot(df3['Magnetic Field Values'], df3['ESR Values'], color='r')
        labels = [labels, 'Reg 3']
    if(i4.get()):
        ax.plot(df4['Magnetic Field Values'], df4['ESR Values'], color='c')
        labels = [labels, 'Reg 4']
    if(i5.get()):
        ax.plot(df5['Magnetic Field Values'], df5['ESR Values'], color='m')
        labels = [labels, 'Reg 5']
    if(i6.get()):
        ax.plot(df6['Magnetic Field Values'], df6['ESR Values'], color='y')
        labels = [labels, 'Reg 6']
    if(i7.get()):
        ax.plot(df7['Magnetic Field Values'], df7['ESR Values'], color='k')
        labels = [labels, 'Reg 7']
    if(i8.get()):
        ax.plot(df8['Magnetic Field Values'],
                df8['ESR Values'], color='sienna')
        labels = [labels, 'Reg 8']
    if(i9.get()):
        ax.plot(df9['Magnetic Field Values'],
                df9['ESR Values'], color='turquoise')
        labels = [labels, 'Reg 9']
    if(i10.get()):
        ax.plot(df10['Magnetic Field Values'],
                df10['ESR Values'], color='fuchsia')
        labels = [labels, 'Reg 10']

    plot1 = FigureCanvasTkAgg(figure, window)
    plot1.get_tk_widget().grid(row=0, column=2,rowspan = 20)
    ax.legend(labels)
    ax.set_xlabel('Magnetic Field (T)')
    ax.set_title('Magnetic Field Vs. ESR')


def import_txt_data1():
    global v1
    txt_file_path1 = askopenfilename()

    v1.set(txt_file_path1)

    global df1
    df1 = pd.read_csv(txt_file_path1, names=[
        'ESR Values'], skiprows=4, skipfooter=16)
    df1.insert(0, "Magnetic Field Values", range(
        df1['ESR Values'].size), True)
    print(df1)
    replot()


def import_txt_data2():
    global v2
    txt_file_path2 = askopenfilename()

    v2.set(txt_file_path2)

    global df2
    df2 = pd.read_csv(txt_file_path2, names=[
        'ESR Values'], skiprows=4, skipfooter=16)
    df2.insert(0, "Magnetic Field Values", range(
        df2['ESR Values'].size), True)
    print(df2)
    replot()


def import_txt_data3():
    global v3
    txt_file_path3 = askopenfilename()

    v3.set(txt_file_path3)

    global df3
    df3 = pd.read_csv(txt_file_path3, names=[
        'ESR Values'], skiprows=4, skipfooter=16)
    df3.insert(0, "Magnetic Field Values", range(
        df3['ESR Values'].size), True)
    print(df3)
    replot()


def import_txt_data4():
    global v4
    txt_file_path4 = askopenfilename()

    v4.set(txt_file_path4)

    global df4
    df4 = pd.read_csv(txt_file_path4, names=[
        'ESR Values'], skiprows=4, skipfooter=16)
    df4.insert(0, "Magnetic Field Values", range(
        df4['ESR Values'].size), True)
    print(df4)
    replot()


def import_txt_data5():
    global v5
    txt_file_path5 = askopenfilename()

    v5.set(txt_file_path5)

    global df5
    df5 = pd.read_csv(txt_file_path5, names=[
        'ESR Values'], skiprows=4, skipfooter=16)
    df5.insert(0, "Magnetic Field Values", range(
        df5['ESR Values'].size), True)
    print(df5)
    replot()


def import_txt_data6():
    global v6
    txt_file_path6 = askopenfilename()

    v6.set(txt_file_path6)

    global df6
    df6 = pd.read_csv(txt_file_path6, names=[
        'ESR Values'], skiprows=4, skipfooter=16)
    df6.insert(0, "Magnetic Field Values", range(
        df6['ESR Values'].size), True)
    print(df6)
    replot()


def import_txt_data7():
    global v7
    txt_file_path7 = askopenfilename()

    v7.set(txt_file_path7)

    global df7
    df7 = pd.read_csv(txt_file_path7, names=[
        'ESR Values'], skiprows=4, skipfooter=16)
    df7.insert(0, "Magnetic Field Values", range(
        df7['ESR Values'].size), True)
    print(df7)
    replot()


def import_txt_data7():
    global v7
    txt_file_path7 = askopenfilename()

    v7.set(txt_file_path7)

    global df7
    df7 = pd.read_csv(txt_file_path7, names=[
        'ESR Values'], skiprows=4, skipfooter=16)
    df7.insert(0, "Magnetic Field Values", range(
        df7['ESR Values'].size), True)
    print(df7)
    replot()


def import_txt_data8():
    global v8
    txt_file_path8 = askopenfilename()

    v8.set(txt_file_path8)

    global df8
    df8 = pd.read_csv(txt_file_path8, names=[
        'ESR Values'], skiprows=4, skipfooter=16)
    df8.insert(0, "Magnetic Field Values", range(
        df8['ESR Values'].size), True)
    print(df8)
    replot()


def import_txt_data9():
    global v9
    txt_file_path9 = askopenfilename()

    v9.set(txt_file_path9)

    global df9
    df9 = pd.read_csv(txt_file_path9, names=[
        'ESR Values'], skiprows=4, skipfooter=16)
    df9.insert(0, "Magnetic Field Values", range(
        df9['ESR Values'].size), True)
    print(df9)
    replot()


def import_txt_data10():
    global v10
    txt_file_path10 = askopenfilename()

    v10.set(txt_file_path10)

    global df10
    df10 = pd.read_csv(txt_file_path10, names=[
        'ESR Values'], skiprows=4, skipfooter=16)
    df10.insert(0, "Magnetic Field Values", range(
        df10['ESR Values'].size), True)
    print(df10)
    replot()


window = tk.Tk()

global i1
global i2
global i3
global i4
global i5
global i6
global i7
global i8
global i9
global i10
i1 = IntVar()
i2 = IntVar()
i3 = IntVar()
i4 = IntVar()
i5 = IntVar()
i6 = IntVar()
i7 = IntVar()
i8 = IntVar()
i9 = IntVar()
i10 = IntVar()


label1 = tk.Label(text="Register 1:")
label1.grid(row=0, column=0)
v1 = tk.StringVar()
entry1 = tk.Entry(window, textvariable=v1).grid(row=0, column=1)
tk.Button(window, text='Browse Data Set',
          command=import_txt_data1).grid(row=1, column=0)
tk.Checkbutton(window, text='Graph',
               command=replot, variable=i1).grid(row=1, column=1)

label2 = tk.Label(text="Register 2:")
label2.grid(row=2, column=0)
v2 = tk.StringVar()
entry2 = tk.Entry(window, textvariable=v2).grid(row=2, column=1)
tk.Button(window, text='Browse Data Set',
          command=import_txt_data2).grid(row=3, column=0)
tk.Checkbutton(window, text='Graph',
               command=replot, variable=i2).grid(row=3, column=1)

label3 = tk.Label(text="Register 3:")
label3.grid(row=4, column=0)
v3 = tk.StringVar()
entry3 = tk.Entry(window, textvariable=v3).grid(row=4, column=1)
tk.Button(window, text='Browse Data Set',
          command=import_txt_data3).grid(row=5, column=0)
tk.Checkbutton(window, text='Graph',
               command=replot, variable=i3).grid(row=5, column=1)

label4 = tk.Label(text="Register 4:")
label4.grid(row=6, column=0)
v4 = tk.StringVar()
entry4 = tk.Entry(window, textvariable=v4).grid(row=6, column=1)
tk.Button(window, text='Browse Data Set',
          command=import_txt_data4).grid(row=7, column=0)
tk.Checkbutton(window, text='Graph',
               command=replot, variable=i4).grid(row=7, column=1)

label5 = tk.Label(text="Register 5:")
label5.grid(row=8, column=0)
v5 = tk.StringVar()
entry5 = tk.Entry(window, textvariable=v5).grid(row=8, column=1)
tk.Button(window, text='Browse Data Set',
          command=import_txt_data5).grid(row=9, column=0)
tk.Checkbutton(window, text='Graph',
               command=replot, variable=i5).grid(row=9, column=1)

label6 = tk.Label(text="Register 6:")
label6.grid(row=10, column=0)
v6 = tk.StringVar()
entry6 = tk.Entry(window, textvariable=v6).grid(row=10, column=1)
tk.Button(window, text='Browse Data Set',
          command=import_txt_data6).grid(row=11, column=0)
tk.Checkbutton(window, text='Graph',
               command=replot, variable=i6).grid(row=11, column=1)

label7 = tk.Label(text="Register 7:")
label7.grid(row=12, column=0)
v7 = tk.StringVar()
entry7 = tk.Entry(window, textvariable=v7).grid(row=12, column=1)
tk.Button(window, text='Browse Data Set',
          command=import_txt_data7).grid(row=13, column=0)
tk.Checkbutton(window, text='Graph',
               command=replot, variable=i7).grid(row=13, column=1)

label8 = tk.Label(text="Register 8:")
label8.grid(row=14, column=0)
v8 = tk.StringVar()
entry8 = tk.Entry(window, textvariable=v8).grid(row=14, column=1)
tk.Button(window, text='Browse Data Set',
          command=import_txt_data8).grid(row=15, column=0)
tk.Checkbutton(window, text='Graph',
               command=replot, variable=i8).grid(row=15, column=1)

label9 = tk.Label(text="Register 9:")
label9.grid(row=16, column=0)
v9 = tk.StringVar()
entry9 = tk.Entry(window, textvariable=v9).grid(row=16, column=1)
tk.Button(window, text='Browse Data Set',
          command=import_txt_data9).grid(row=17, column=0)
tk.Checkbutton(window, text='Graph',
               command=replot, variable=i9).grid(row=17, column=1)

label10 = tk.Label(text="Register 10:")
label10.grid(row=18, column=0)
v10 = tk.StringVar()
entry10 = tk.Entry(window, textvariable=v10).grid(row=18, column=1)
tk.Button(window, text='Browse Data Set',
          command=import_txt_data10).grid(row=19, column=0)
tk.Checkbutton(window, text='Graph',
               command=replot, variable=i10).grid(row=19, column=1)

window.mainloop()
