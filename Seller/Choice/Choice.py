from Support_files.imports import *

#def back():
#    current_directory = os.getcwd()
#
#    # Относительный путь к main.py
#    main_script_relative_path = "../login.py"  # Предполагается, что main.py находится на уровне выше относительно login.py
#    # Формируем абсолютный путь к main.py
#    main_script_path = os.path.join(current_directory, main_script_relative_path)
#
#    # Открываем main.py
#    subprocess.Popen(["python", main_script_path])

def back():
    main_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "login.py"))
    print(main_file_path)

    path = main_file_path
    subprocess.run(["python",path])
    root.deiconify(path)
    root.destroy()

def open_search():
    path = "Seller\\Choice\\order_window.py"
    subprocess.Popen(["python",path])
    root.withdraw()


def open():
    pass

def regis():
    path = "Seller\\Choice\\regist.py"
    subprocess.Popen(["python",path])
    root.withdraw()


root = tk.Tk()
window_width = 250
window_height = 250
root.resizable(False,False)
fun.center_window(root,window_width,window_height)
root.title("Окно выбора")

btn_Orders = ttk.Button(text="Заказы",command=open_search,width=15)
btn_Orders.pack(pady = 5)

#btn_Check = ttk.Button(text="Обновление",command=click_Change,width=15)
#btn_Check.pack(pady = 5)

btn_Check = ttk.Button(text="Рег.Клиента",command=regis,width=15)
btn_Check.pack(pady = 5)

btn_back = ttk.Button(text="<",command=back)
btn_back.place(x= 5,y = 10,width = 30)
root.mainloop()