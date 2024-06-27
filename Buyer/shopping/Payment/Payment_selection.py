import subprocess
from Support_files.imports import *
import tkinter as tk
from tkinter import ttk
import pickle

root = tk.Tk()

fun.center_window(root,250,250)
root.title("СпортМастер")
def card():
    notification = ttk.tkinter.messagebox.showinfo("Оплата картой", "Поднесите карту к терминалу")

def nal():
    notification = ttk.tkinter.messagebox.showinfo("Оплата наличными", "Пройдите к свободной кассе")


def krip():
    notification = ttk.tkinter.messagebox.showinfo("Оплата СБП", "Отсканируйте QR-код")


btn_card = ttk.Button(text="Оплата картой",width=20,command=card)
btn_card.place(x = 120,y=20, anchor="center")

btn_nal = ttk.Button(text="Оплата наличными",width=20,command=nal)
btn_nal.place(x = 120,y=50, anchor="center")

btn_krip = ttk.Button(text="Оплата СБП",width=20,command=krip)
btn_krip.place(x = 120,y=80, anchor="center")

root.mainloop()