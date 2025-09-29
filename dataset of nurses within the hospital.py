import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy.f2py.symbolic import as_eq

df = pd.read_csv("/Users/becky/Downloads/nurse_attrition 01 10 2025 (1).csv")


df.columns = df.columns.str.strip().str.lower()
if "attrition" not in df.columns:
    raise KeyError("Dataset must contain an 'attrition' column!")

attrition_rate = df["attrition"].astype(str).str.strip().str.lower()
print('unique attrition values:', df['attrition'].unique())  # debu
attrition_rate = df['attrition'].value_counts(normalize=True).get('yes', 0) * 100


avg_satisfaction = df['worklifebalance'].mean()

dept_count = df['department'].value_counts()

root = tk.Tk()
root.title('Healthcare Dashboard')
root.geometry('200x500')

def show_dashboard():
    popup = tk.Toplevel()
    popup.title('Healthcare summary')
    popup.geometry('1000x500')

    fig, axes = plt.subplots(1 , 2, figsize = (10,6))

    axes[0].bar(['Average Satisfaction'], [avg_satisfaction], color= 'purple')
    axes[0].set_ylim(0,5)
    axes[0].set_title('Average Satisfaction')

    axes[1].pie(df['attrition'].value_counts(), labels=df['attrition'].value_counts().index,
                autopct='%1.1f%%', colors=['lightcoral', 'lightgreen'])
    axes[1].set_title("Attrition Rate")

    canvas = FigureCanvasTkAgg(fig, master=popup)
    canvas.draw()
    canvas.get_tk_widget().pack()

def show_piechart():
    popup = tk.Toplevel()
    popup.title('Department Distribution')
    popup.geometry('200x500')

    dept_counts = df['department'].value_counts()
    fig, ax = plt.subplots(figsize=(12, 8))

    colors = plt.cm.tab20.colors

    explode = [0.05] * len(dept_counts)

    ax.pie(dept_counts,
        labels=dept_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors[:len(dept_counts)],
        explode=explode,
        shadow=True)

    ax.set_title('Department Distribution of nurses within the department')

    canvas = FigureCanvasTkAgg(fig, master=popup)
    canvas.draw()
    canvas.get_tk_widget().pack()

Btn1 = tk.Button(root, text="Show Dashboard", command=show_dashboard)
Btn1.pack()

btn2 = tk.Button(root, text="Show Dashboard", command=show_piechart)
btn2.pack()

root.mainloop()
