#Разработать программу с применением пакета tk, взяв в качестве условия одну
#любую задачу из ПЗ №№ 2 – 9.

import tkinter as tk
from tkinter import ttk

def f(s):
    try: return "Число является четным" if int(s) % 2 == 0 else "Число не является четным"
    except: return "Не число"

root = tk.Tk()
root.title("Проверка чётности")
root.geometry("200x80")

s = tk.StringVar()

entry = tk.Entry(root)
btn = tk.Button(root, text="Click", command=lambda: s.set(f(entry.get())))
lbl = tk.Label(root, textvariable=s)
entry.pack()
btn.pack()
lbl.pack()
root.mainloop()