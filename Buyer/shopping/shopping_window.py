import time

from Support_files.imports import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import os
import pickle

def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def save_variables(var1, var2, var3,var4):
    data = {'var1': var1, 'var2': var2, 'var3': var3, 'var4': var4}
    with open('data.pickle', 'wb') as file:
        pickle.dump(data, file)



klik = 0
gl_st = 0
gl_st_list = []
gl_product_name_list = []

n = 0

def add_to_cart(product_name,prise):
    global klik,gl_st,gl_st_list,gl_product_name_list,n
    klik += 1
    gl_st += prise
    gl_product_name_list.append(product_name)
    gl_st_list.append(prise)
    btn.configure(text=f"Корзина {klik}")
    print(f"Товар '{product_name}' добавлен в корзину цена {prise}")
    print(f"сумма {gl_st}")
    save_variables(klik, gl_st, gl_product_name_list,gl_st_list)
    n += prise
    lb_summ.configure(text=f"Сумма: {n}")





root = tk.Tk()
root.title("Спортивный магазин")
width = 800
height = 600
fun.center_window(root,800,600)

root.bind_all("<MouseWheel>", on_mousewheel)

def Basket():

    path = "Buyer\\shopping\\Payment\\Basket.py"
    subprocess.Popen(["python",path])
    root.withdraw()

btn = ttk.Button(text = "Корзина",command=Basket)
btn.pack(anchor="ne")
lb_summ = tk.Label(text=f"",font=("Arial",20))
lb_summ.pack(anchor="ne")

canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

frame = ttk.Frame(canvas)
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

canvas.create_window((0, 0), window=frame, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_frame_configure)

db_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "entrance.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT Product, Price, Size, Manufacturer FROM Product")
products = cursor.fetchall()
def show_product_card(product, row, column):
    card_frame = tk.Frame(frame, borderwidth=4, relief="groove", width=200, height=150)
    card_frame.grid(row=row, column=column, padx=10, pady=10)
    name_label = tk.Label(card_frame, text=f"Название: {product[0]}", wraplength=180, anchor="w")
    name_label.pack(fill=tk.X)

    price_label = tk.Label(card_frame, text=f"Цена: {product[1]}", wraplength=180, anchor="w")
    price_label.pack(fill=tk.X)

    size_label = tk.Label(card_frame, text=f"Размер: {product[2]}", wraplength=180, anchor="w")
    size_label.pack(fill=tk.X)

    manufacturer_label = tk.Label(card_frame, text=f"Производитель: {product[3]}", wraplength=180, anchor="w")
    manufacturer_label.pack(fill=tk.X)

    btn_Basket = ttk.Button(card_frame, text="В корзину", command=lambda st=int(product[1]),prod=product[0]: add_to_cart(prod,st))
    btn_Basket.pack(padx=40, pady=10)


for i, product in enumerate(products):
    row = i // 3
    column = i % 3
    show_product_card(product, row, column)


root.mainloop()
