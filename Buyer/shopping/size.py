
from Support_files.imports import *



root = tk.Tk()
root.resizable(False,False)
root.title("Выбор размера")
width = 500
height = 250
fun.center_window(root,width,height)
def chekbox():
    if ck_man_var.get() == 1:
        ck_girl_var.set(0)
    if ck_girl_var.get() == 1:
        ck_man_var.set(0)

def Clothes():
    Chest_x = int(Chest_combobox.get())
    Pants_x=int(Pants_combobox.get())
    Shoes_x = float(Shoes_combobox.get())
    label_rezult_one = tk.Label(text="")
    #Размер груди и размер майки
    if 86 <= Chest_x < 90:
        label_rezult_one = tk.Label(text=f"При обхвате {Chest_x} ваш размер 44 или XS")
    elif 90 <= Chest_x < 94:
        label_rezult_one = tk.Label(text=f"При обхвате {Chest_x} ваш размер 46 или S")
    elif 94 <= Chest_x < 98:
        label_rezult_one = tk.Label(text=f"При обхвате {Chest_x} ваш размер 48 или M")
    elif 98 <= Chest_x < 102:
        label_rezult_one = tk.Label(text=f"При обхвате {Chest_x} ваш размер 50 или L")
    elif 102 <= Chest_x < 106:
        label_rezult_one = tk.Label(text=f"При обхвате {Chest_x} ваш размер 52 или XL")
    elif 106 <= Chest_x < 110:
        label_rezult_one = tk.Label(text=f"При обхвате {Chest_x} ваш размер 54 или 2XL")
    elif 110 <= Chest_x < 114:
        label_rezult_one = tk.Label(text=f"При обхвате {Chest_x} ваш размер 56 или 3XL")
    elif 114 <= Chest_x < 118:
        label_rezult_one = tk.Label(text=f"При обхвате {Chest_x} ваш размер 58 или 4XL")
    elif 118 <= Chest_x < 122:
        label_rezult_one = tk.Label(text=f"При обхвате {Chest_x} ваш размер 60 или 5XL")
    label_rezult_one.place(x=150,y=120)

    #Размер штанов
    if 76 <= Pants_x < 84:
        label_rezult_one = tk.Label(text=f"При ширине {Pants_x} ваш размер 44 или XS")
    elif 84 <= Pants_x < 88:
        label_rezult_one = tk.Label(text=f"При ширине {Pants_x} ваш размер 46 или S")
    elif 88 <= Pants_x < 92:
        label_rezult_one = tk.Label(text=f"При ширине {Pants_x} ваш размер 48 или M")
    elif 92 <= Pants_x < 100:
        label_rezult_one = tk.Label(text=f"При ширине {Pants_x} ваш размер 50 или L")
    elif 100 <= Pants_x < 106:
        label_rezult_one = tk.Label(text=f"При ширине {Pants_x} ваш размер 52 или XL")
    elif 106 <= Pants_x < 114:
        label_rezult_one = tk.Label(text=f"При ширине {Pants_x} ваш размер 58 или 2XL")
    label_rezult_one.place(x=150,y=140)


    #Размер обуви
    if Shoes_x == 25.0:
        label_rezult_one = tk.Label(text=f"При длине {Shoes_x} ваш размер 39")
    elif Shoes_x == 26.7:
        label_rezult_one = tk.Label(text=f"При длине {Shoes_x} ваш размер 40")
    elif Shoes_x == 26.4:
        label_rezult_one = tk.Label(text=f"При длине {Shoes_x} ваш размер 41")
    elif Shoes_x == 27.1:
        label_rezult_one = tk.Label(text=f"При длине {Shoes_x} ваш размер 42")
    elif Shoes_x == 27.8:
        label_rezult_one = tk.Label(text=f"При длине {Shoes_x} ваш размер 43")
    elif Shoes_x == 28.5:
        label_rezult_one = tk.Label(text=f"При длине {Shoes_x} ваш размер 44")
    elif Shoes_x == 29.2:
        label_rezult_one = tk.Label(text=f"При длине {Shoes_x} ваш размер 45")
    elif Shoes_x == 29.9:
        label_rezult_one = tk.Label(text=f"При длине {Shoes_x} ваш размер 46")
    elif Shoes_x == 30.6:
        label_rezult_one = tk.Label(text=f"При длине {Shoes_x} ваш размер 47")
    elif Shoes_x == 31.3:
        label_rezult_one = tk.Label(text=f"При длине {Shoes_x} ваш размер 48")
    label_rezult_one.place(x=150,y=160)



ck_man_var = tk.IntVar()
ck_man = ttk.Checkbutton(root,text="Мужской",command=chekbox,variable=ck_man_var)
ck_man.pack(anchor = "w")

ck_girl_var = tk.IntVar()
ck_girl = ttk.Checkbutton(root,text="Женский",command=chekbox,variable=ck_girl_var)
ck_girl.place(x=100,y=0)

#Обхват груди
label_Chest = ttk.Label(text="Выберите обхват груди")
label_Chest.place(x=0,y=26)
Size_Chest = [i for i in range(86,123)]
Chest_combobox = ttk.Combobox(values = Size_Chest)

Chest_combobox.place(x=0,y=46)


#Ваш рост
label_Height = ttk.Label(text="Выберите ваш рост")
label_Height.place(x=150,y=26)
Size_Height= [i for i in range(152,200)]+["200 и более"]
Height_combobox = ttk.Combobox(values = Size_Height)
Height_combobox.place(x=150,y=46)


#Размер штанов
label_Pants = ttk.Label(text = "Обхват талии")
label_Pants.place(x=0,y=68)
Size_Pants = [i for i in range(76,115)]
Pants_combobox = ttk.Combobox(values = Size_Pants)
Pants_combobox.place(x=0,y=88)


#Размер обуви
step = 0.7
label_Shoes = ttk.Label(text = "Размер обуви")
label_Shoes.place(x=150,y=68)
Shoes_Pants = [i.round(1) for i in np.arange(25,32,step)]
Shoes_combobox = ttk.Combobox(values = Shoes_Pants)
Shoes_combobox.place(x=150,y=88)


btn_rezult = ttk.Button(text="Узнать свой размер",command=Clothes)
btn_rezult.place(x=150,y=120)

root.mainloop()