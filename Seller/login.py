import os.path
import sqlite3
import subprocess
import sys


from Support_files.imports import *
count = 0
def back():
    main_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "main.py"))

    path = main_file_path
    subprocess.run(["python",path])
    root.deiconify(path)
    root.withdraw()
def click_btn():
    login = entry_login.get()
    password = entry_password.get()

    script_dir = os.path.dirname(__file__)

    project_dir = os.path.dirname(script_dir)
    db_path = os.path.join(project_dir, "data", "entrance.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Seller WHERE login = ? AND password = ?", (login, password))
    select = cursor.fetchone()
    dt = datetime.datetime.now()
    if select is not None:
        messagebox.showinfo("Вход", "Поздравляю, вы вышли на смену!")

        login_time = dt + datetime.timedelta(hours=8)
        cursor.execute("INSERT INTO date (login,start,stop) VALUES(?,?,?)",(login,dt.strftime('%H:%M'),login_time.strftime('%H:%M')))
        conn.commit()
        path = "Seller\\Choice\\Choice.py"
        subprocess.Popen(["python", path])
        root.destroy()
    else:
        global count
        count += 1
        if count < 4:
            label_result.config(text=f"Error, осталось попыток {4-count}", fg="red")
            entry_password.delete(0, tk.END)
            entry_login.delete(0, tk.END)

        else:
            messagebox.showerror("Ошибка","Вы ввели 3 раза не верный пароль")
            root.destroy()

    cursor.close()
    conn.close()

root = tk.Tk()
window_width = 250
window_height = 250
fun.center_window(root,window_width,window_height)
root.resizable(False,False)

root.title("СпортМастер окно продавца")
root.minsize(150,120)

Label_login = ttk.Label(text="Введите логин",font=("Arial",10))
entry_login = ttk.Entry()
Label_login.pack()
entry_login.pack()


label_password = ttk.Label(text="Введите пароль",font=("Arial",10))
entry_password = ttk.Entry()
label_password.pack(pady= (10,0))
entry_password.pack()


btn = ttk.Button(text="Войти",command=click_btn)
btn.pack(pady = 10)
btn.bind("<Enter>",fun.cursor(btn=btn))


label_result = tk.Label(text="",font=("Arial",10))
label_result.pack()


btn_back = ttk.Button(text="<",command=back)
btn_back.place(x= 5,y = 10,width = 30)
if __name__ == "__main__":
    root.mainloop()