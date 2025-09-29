from sys import displayhook
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backend_bases import button_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import title
from pyparsing import pa_call_line_synth

root = tk.Tk()
root.title('Marital Status of Employment')
root.geometry('100x600')

df = pd.read_csv("/Users/becky/Downloads/nurse_attrition 01 10 2025 (1).csv")
df = df.dropna(subset=['MaritalStatus', 'Gender'])

marital_status = df['MaritalStatus'].value_counts()

fig, ax = plt.subplots(figsize=(10,5))
ax.bar(marital_status.index, marital_status.values, color='blue', edgecolor='black')
ax.set_title('Martial status of Employees')
ax.set_xlabel('Martial status')
ax.set_ylabel('Number of employees')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(pady=20)

label = tk.Label(root, text="Department", font=("Arial", 18))
label.pack(pady=10)

btn = tk.Button(root, text='display bar chart', command=lambda: root.destroy())
btn.pack(pady=10)

root.mainloop()