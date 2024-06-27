import subprocess

from Support_files.imports import *
def clik_product():
    path = "Buyer\\shopping\\shopping_window.py"
    subprocess.Popen(["python",path])
    root.withdraw()
def clic_consultant():
    messagebox.showinfo("Выбор консультанта","Ожидайте скоро к вам подойдут")
def clik_size():
    answer = messagebox.askyesno("Выбор размера","Попробуйте тестовый подбор размера")
    if answer:
        path = "Buyer\\shopping\\size.py"
        subprocess.Popen(["python",path])
        root.withdraw()




root = tk.Tk()
window_width = 250
window_height = 250
root.resizable(False,False)
root.title("Спортмастер")
fun.center_window(root,window_width,window_height)
label1 = tk.Label(text="Выберите")
label1.pack()

btn_consultant = ttk.Button(text="Позвать консультанта",
                           width=20,
                           command=clic_consultant)
btn_consultant.pack(pady=10)
btn_consultant.bind("<Enter>",fun.cursor(btn=btn_consultant))


btn_product = ttk.Button(text="Выбрать товар",
                        width=20,
                        command=clik_product)
btn_product.pack(pady=10)
btn_product.bind("<Enter>",fun.cursor(btn=btn_product))



btn_size = ttk.Button(text="Узнать размер",
                        width=20,
                        command=clik_size)
btn_size.pack(pady=10)
btn_size.bind("<Enter>",fun.cursor(btn=btn_size))



root.mainloop()