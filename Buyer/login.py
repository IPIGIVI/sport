from Support_files.imports import *
count = 0
def click_btn():
    login = entry_login.get()
    password = entry_password.get()

    script_dir = os.path.dirname(__file__)
    project_dir = os.path.dirname(script_dir)
    db_path = os.path.join(project_dir, "data", "entrance.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Buyer WHERE login = ? and password = ?",(login,password))
    select = cursor.fetchone()

    if select is not None:
        path = "Buyer\\Product and consultant.py"
        subprocess.Popen(["python",path])
        root.destroy()
    else:
        global count
        count += 1
        if count < 4:
            label_result.config(text=f"Error, осталось попыток {4-count}", fg="red")
            entry_password.delete(0,tk.END)
            entry_login.delete(0,tk.END)

        else:
            messagebox.showerror("Ошибка","Вы ввели 3 раза не верный пароль")
            root.destroy()

    cursor.close()
    conn.close()
def regis():
    messagebox.showinfo("Регистриция","Для корректной регистрации обратитесь к оператору")
root = tk.Tk()

window_width = 250
window_height = 250
fun.center_window(root,window_width,window_height)
root.title("СпортМастер окно покупателя")
root.minsize(150,120)
root.resizable(False,False)

Label_login = ttk.Label(text="Введите логин",font=("Arial",10))
entry_login = ttk.Entry()
Label_login.pack()
entry_login.pack()


label_password = ttk.Label(text="Введите пароль",font=("Arial",10))
entry_password = ttk.Entry()
label_password.pack(pady = (10,0))
entry_password.pack()

btn = ttk.Button(text="Войти",command=click_btn,width=20)
btn.pack(pady = 10)
btn.bind("<Enter>",fun.cursor(btn =btn))


btn_reg = ttk.Button(text="Регистрация",command=regis,width=20)
btn_reg.pack()
#btn_reg.bind("<Enter>",fun.cursor(btn =btn))

label_result = tk.Label(text="",font=("Arial",10))
label_result.pack()

root.mainloop()