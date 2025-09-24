from pickle import EMPTY_LIST
from tkinter.font import names

import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("CSV bar chart")
root.geometry("300x300")
df = pd.read_csv("/Users/becky/Downloads/nurse_attrition 01 10 2025 (1).csv")
print(df.head())
head_text = df.head().to_string()

label = tk.Label(root, text=head_text, justify=tk.LEFT)
label.pack()


def bar_chart():

        df = pd.read_csv("/Users/becky/Downloads/nurse_attrition 01 10 2025 (1).csv")
        df = df.dropna(subset=['EmployeeID', 'Age'])
        EmployeeID = df['EmployeeID']
        ages = df['Age']

        fig, ax = plt.subplots(figsize=(10,5))
        ax.bar(EmployeeID, ages, color='purple', edgecolor='black')
        ax.set_title('Age Distribution')
        ax.set_xlabel('EmployeeID')
        ax.set_ylabel('Age')
        plt.show()

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget()

btn_barchart = tk.Button(root, text='Display Bar Chart', command=bar_chart)
btn_barchart.pack(pady=10)


def open():
    top = tk.Toplevel()
    label = tk.Label(top, text="Hello there").pack()

    button = tk.Button(top, text="open an second window", command=open())
    button.pack()

root.mainloop()


