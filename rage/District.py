from rage.Office import Office
from rage.Werehouse import Werehouse
from rage.Rezidential import Rezidential
from tkinter import *


#Инициализация классов
off = Office()
were = Werehouse()
resid = Rezidential()


#главное окно
class MainApp(Tk):
    def __init__(root, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        # Создаём шаблон формы, главный бокс
        root.title("План ФПК 6 факультета")
        root.geometry("500x450")

        # Запрещаем менять размер окна
        root.resizable(False, False)

        # Добавляем кнопку выхода
        btn_exit = Button(text="Close",
                          background="#D3D3D3",
                          foreground="#000000",
                          padx="20",
                          command=quit)
        btn_exit.place(x=405, y=400)

        #Создаем TextBox для вывода данных
        textbox = Text(root,
                       width=55,
                       height=15)
        textbox.pack()

        #Функция для удаления содержимого TextBox
        def delete_text():
            textbox.delete(1.0, END)

        #Добавляем кнопку очистки TextBox
        button_clear = Button(root,
                               text='Clear',
                               command=delete_text,
                               background="#D3D3D3",
                               foreground="#000000",
                               padx="20")
        button_clear.place(x=405, y=370)

        #Кнопка вывода данных Werehouse
        button_output = Button(root,
                         text='Werehouse',
                         command=lambda: print(were.info_werehouse(), were.num_rooms(), were.people(), were.size_werehouse()),
                         background = "#D3D3D3",
                         foreground = "#000000",
                         padx = "20")
        button_output.place(x=340, y=270)

        #Кнопка вывода данных Office
        button_output = Button(root,
                               text='Office',
                               command=lambda: print(off.info_office(), off.num_rooms(), off.people(), off.size_office()),
                               background="#D3D3D3",
                               foreground="#000000",
                               padx="33")

        button_output.place(x=50, y=270)

        #Кнопка вывода данных Rezidential
        button_output = Button(root,
                               text='Rezidential',
                               command=lambda: print(resid.info_rezidential_(), resid.num_rooms(), resid.people(), resid.size_residential()),
                               background="#D3D3D3",
                               foreground="#000000",
                               padx="20")

        button_output.place(x=198, y=270)

        #Функция вывода данных
        def redirector(inputStr):
            textbox.insert(INSERT, inputStr)
        sys.stdout.write = redirector

# Запуск программы
if __name__ == '__main__':
    MainApp().mainloop()



