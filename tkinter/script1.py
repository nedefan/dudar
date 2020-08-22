from tkinter import *
import webbrowser
from tkinter import ttk

app = Tk()
app.title("Поисковая система")  # Название окна
app.configure(background='#ececec')

app_name = ttk.Label(app, text='Поисковое приложение', font='verdana 24', foreground='#333')
app_name.grid(row=0, column=2)

search_label = ttk.Label(app, text='Поиск')
search_label.grid(row=1, column=1)

text_field = ttk.Entry(app, width=50)
text_field.grid(row=1, column=2)

search_engine = StringVar()
search_engine.set("google")  # Выбираем приложение для поиска в начале работы программы


def search():
    if text_field.get().strip() != "":  # Проверяем чтобы строка поиска не была пустой
        if search_engine.get() == "google":
            webbrowser.open('https://www.google.com/search?q=' + text_field.get())  # Функция открывает новое
            # окно в браузере и передает запрос по адресу извлекая его из текстового поля
        elif search_engine.get() == "yandex":
            webbrowser.open('https://www.yandex.ru/search/?text=' + text_field.get())


def search_btn():
    search()


def enter_btn(event):
    search()


btn_search = ttk.Button(app, text="Найти", width=10, command=search)  # Выполняет функцию при нажатии кнопки
btn_search.grid(row=1, column=4)

text_field.bind('<Return>', enter_btn)  # Выполняет функцию при нажатии кнопки Enter в данном окне

radio_google = ttk.Radiobutton(app, text='Google', value='google', variable=search_engine)
radio_google.grid(row=0, column=3, sticky=W)  # Параметр sticky Запад
radio_google = ttk.Radiobutton(app, text='Yandex', value='yandex', variable=search_engine)
radio_google.grid(row=1, column=3, sticky=E)  # Параметр sticky Восток

app.wm_attributes('-topmost', True)  # Выводит окно поверх других окон

app.mainloop()
