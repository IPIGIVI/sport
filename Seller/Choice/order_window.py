import random

from Support_files.imports import *



# Определение текущего расположения скрипта
script_dir = os.path.dirname(__file__)

# Поднятие на два уровня выше в директорию проекта
project_dir = os.path.dirname(os.path.dirname(script_dir))

# Путь к базе данных
db_path = os.path.join(project_dir, "data", "entrance.db")


class zakaz:
    db_name = db_path

    def __init__(self, window):

        self.wind = window
        self.wind.title('Спортмастер')

        # создание элементов для ввода слов и значений
        frame = LabelFrame(self.wind, text='Введите новую сумму')
        frame.grid(row=0, column=0, columnspan=3, pady=20)
        Label(frame, text='Сумма: ').grid(row=1, column=0)
        self.summ = Entry(frame)
        self.summ.focus()
        self.summ.grid(row=1, column=1)
        Label(frame, text='Статус: ').grid(row=2, column=0)
        self.status = Entry(frame)
        self.status.grid(row=2, column=1)
        ttk.Button(frame, text='Сохранить', command=self.add_summ).grid(row=3, columnspan=2, sticky=W + E)
        self.message = Label(text='', fg='green')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W + E)
        # таблица слов и значений
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Сумма', anchor=CENTER)
        self.tree.heading('#1', text='Статус оплаты', anchor=CENTER)

        # кнопки редактирования записей
        ttk.Button(text='Удалить', command=self.delete_summ).grid(row=5, column=0, sticky=W + E)
        ttk.Button(text='Изменить', command=self.edit_summ).grid(row=5, column=1, sticky=W + E)

        # заполнение таблицы
        self.get_summs()

    # подключение и запрос к базе
    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # заполнение таблицы словами и их значениями
    def get_summs(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = 'SELECT * FROM zakaz ORDER BY summ DESC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=row[2])

    # валидация ввода
    def validation(self):
        return len(self.summ.get()) != 0 and len(self.status.get()) != 0

    # добавление нового слова
    def add_summ(self):
        if self.validation():
            query = 'INSERT INTO zakaz VALUES(NULL, ?, ?)'
            parameters = (self.summ.get(), self.status.get())
            self.run_query(query, parameters)
            self.message['text'] = 'слово {} добавлено в список'.format(self.summ.get())
            self.summ.delete(0, END)
            self.status.delete(0, END)
        else:
            self.message['text'] = 'введите сумму и статус'
        self.get_summs()

    # удаление слова
    def delete_summ(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]

        except IndexError as e:
            self.message['text'] = 'Выберите заказ, который нужно удалить'
            return
        self.message['text'] = ''
        summ = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM zakaz WHERE summ = ?'
        self.run_query(query, (summ,))
        self.message['text'] = 'Заказ {} успешно удаленен'.format(summ)
        self.get_summs()

    # рeдактирование слова и/или значения
    def edit_summ(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Выберите заказ для изменения'
            return
        word = self.tree.item(self.tree.selection())['text']
        old_meaning = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Изменить заказ'

        Label(self.edit_wind, text='Прежняя сумма:').grid(row=0, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=word), state='readonly').grid(row=0,
                                                                                                         column=2)

        Label(self.edit_wind, text='Новая сумма:').grid(row=1, column=1)
        # предзаполнение поля
        new_word = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=word))
        new_word.grid(row=1, column=2)

        Label(self.edit_wind, text='Прежнее значение:').grid(row=2, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=old_meaning), state='readonly').grid(row=2,
                                                                                                                column=2)

        Label(self.edit_wind, text='Новое значение:').grid(row=3, column=1)
        # предзаполнение поля
        new_meaning = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=old_meaning))
        new_meaning.grid(row=3, column=2)

        Button(self.edit_wind, text='Изменить',
               command=lambda: self.edit_records(new_word.get(), word, new_meaning.get(), old_meaning)).grid(row=4,
                                                                                                             column=2,
                                                                                                             sticky=W)
        self.edit_wind.mainloop()

    # внесение изменений в базу
    def edit_records(self, new_word, word, new_meaning, old_meaning):
        query = 'UPDATE zakaz SET summ = ?, status = ? WHERE summ = ? AND status = ?'
        parameters = (new_word, new_meaning, word, old_meaning)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'слово {} успешно изменено'.format(word)
        self.get_summs()


if __name__ == '__main__':
    window = Tk()
    application = zakaz(window)
    window.mainloop()
