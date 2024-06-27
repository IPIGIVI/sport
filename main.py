from Support_files.imports import *

def click_Buyer():
    path = "Buyer\\login.py"
    subprocess.Popen(["python",path])
    root.withdraw()
def click_Saller():
    path = "Seller\\login.py"
    subprocess.Popen(["python",path])
    root.withdraw()

root = tk.Tk()
window_width = 250
window_height = 250
fun.center_window(root,window_width,window_height)
root.resizable(False,False)

root.title("СпортМастер")
root.minsize(150,120)


Label_login = tk.Label(text="Выберите должность",font=("Arial",10))
Label_login.pack()

btn = ttk.Button(text="Покупатель",command=click_Buyer,width=20)
btn.pack(pady = 10)
btn.bind("<Enter>",fun.cursor(btn=btn))

btn = ttk.Button(text="Продавец",command=click_Saller,width=20)
btn.pack(pady = 10)
btn.bind("<Enter>",fun.cursor(btn=btn))


root.mainloop()