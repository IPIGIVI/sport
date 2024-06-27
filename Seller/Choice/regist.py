import sqlite3

from Support_files.imports import *


root = tk.Tk()
fun.center_window(root,250,250)
root.resizable(False,False)
root.title("Регистрация пользователя")

def reg():
    login = en_log.get()
    password = en_pas.get()
    age = en_age.get()
    gender = en_gen.get()
    if login == "" or password == '' or age == '' or gender == '':
        lb = tk.Label(text="Ошибка",fg='red')
        lb.place(x = 105,y = 125)
    else:
        # Получение пути к текущей директории скрипта
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Формирование относительного пути к файлу базы данных
        db_path = os.path.join(current_dir, '..', '..', 'data', 'entrance.db')

        # Подключение к базе данных
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Ваши SQL-запросы
        cursor.execute("INSERT INTO Buyer (login,password,age,gender) VALUES (?,?,?,?)", (login, password, age, gender))

        # Сохранение изменений и закрытие соединения
        conn.commit()
        conn.close()


#Логин
lb_log=ttk.Label(text="Логин")
lb_log.place(x = 0,y = 0)

#Окно логина
en_log = ttk.Entry()
en_log.place(x = 80,y =0)

#Пароль
lb_pass = ttk.Label(text="Пароль")
lb_pass.place(x = 0,y = 30)

#Окно Пароля
en_pas = ttk.Entry()
en_pas.place(x = 80,y = 30)

#Введите возраст покупателя
lb_age = ttk.Label(text="Возраст")
lb_age.place(x = 0,y = 60)

#Окно возраста
a = [i for i in range(18,100)]
en_age = ttk.Combobox(values=a)
en_age.place(x = 80,y = 60,width = 50)


# Гендр
a = ["Муж","Жен"]
en_gen=ttk.Combobox(values=a)
en_gen.place(x = 155,y = 60,width = 50)



#Кнопка Зарегистрировать
but = ttk.Button(text="Регистрация",command=reg)
but.place(x = 90,y = 100)
but.bind("<Enter>",fun.cursor(btn=but))

root.mainloop()