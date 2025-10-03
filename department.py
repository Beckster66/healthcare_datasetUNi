import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


df = pd.read_csv("/Users/becky/Downloads/nurse_attrition 01 10 2025 (1).csv")
print(df['Department'].unique())
print(df['Department'].value_counts())

root = tk.Tk()
root.title("What departments are in the hospital dataset")
root.geometry("400x400")

def Show_Piechart():
    dept_counts = df['Department'].value_counts()

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title('Department Distribution of nurses within the department')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

label = tk.Label(root, text="Department Distribution of nurses", font=("Arial", 20))
label.pack(pady=10)

click = tk.StringVar(root)
departments = df['Department'].unique().tolist()
click.set(departments[0])

drop = tk.OptionMenu(root, click, *departments)
drop.pack(pady=10)

pie_btn = tk.Button(root, text="Show Pie chart", command=Show_Piechart)
pie_btn.pack(pady=10)

root.mainloop()



