import subprocess

from Support_files.imports import *
import tkinter as tk
from tkinter import ttk

import pickle

def load_variables():
    with open('data.pickle', 'rb') as file:
        data = pickle.load(file)
        return data['var1'], data['var2'], data['var3'], data['var4']

# Загружаем переменные
var1, var2, var3,var4= load_variables()
number_ord = 0


def bd():
    global number_ord, var2
    number_ord += 1
    status = "Не"  # Corrected spelling
    db_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "entrance.db")

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO zakaz(order_number, summ, status) VALUES(NULL, ?, ?)",
                           (str(var2), status))
            conn.commit()
    except sqlite3.Error as e:
        print("Error inserting data:", e)
def py():
    path = 'Buyer\\shopping\\Payment\\Payment_selection.py'
    subprocess.Popen(["python",path])
    bd()
    root.withdraw()

root = tk.Tk()
root.title("СпортМастер")
fun.center_window(root,500,400)
label_tovar = ttk.Label(text=f"Товары:")
label_tovar.place(x= 10,y= 20)

label_coin = ttk.Label(text=f"Цена:")
label_coin.place(x= 150,y= 20)

label_coin = ttk.Label(text=f"Итог:")
label_coin.place(x= 350,y= 20)
label_coin = ttk.Label(text=var2)
label_coin.place(x= 350,y= 50)

but_coin = ttk.Button(text="Оплата",command=py)
but_coin.place(x = 350,y = 70)
def otobrajenie(var1, var2, var3,var4):
    count = 30
    for i in range(var1):
        count += 20
        label_coin = ttk.Label(text=var3[i])
        label_coin.place(x=10, y=count)

        label_p = ttk.Label(text=var4[i])
        label_p.place(x= 150,y= count)

otobrajenie(var1,var2, var3,var4)


print(f'товаров {var1} на сумму - {var2}')


root.mainloop()