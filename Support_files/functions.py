#окно появляеться по середине экрана
def center_window(window,width,height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width / 2) - (width /2)
    y = (screen_height / 2) - (height /2)

    window.geometry("%dx%d+%d+%d" %(width,height,x,y))

# при наведении меняеться крусор
def cursor(btn):
    btn.config(cursor="hand2")

