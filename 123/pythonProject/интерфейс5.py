from tkinter import *

def exit_game():
    root.destroy()

def open_difficulty_window():
    root.withdraw()  # Скрываем текущее окно
    difficulty_window = Toplevel()
    difficulty_window.title('Выбор уровня сложности')
    difficulty_window.geometry('913x580+300+100')
    difficulty_window.resizable(0, 0)

    difficulty_window.image = PhotoImage(file='экрформа2.png')
    bg_logo = Label(difficulty_window, image=difficulty_window.image)
    bg_logo.place(x=0, y=0, relwidth=1, relheight=1)

    # Добавление кнопок на второе окно
    button_left = Button(difficulty_window, text='Уровень 1', bg='rosybrown2', fg='salmon4',
                         font=('Comic Sans MS', 20), command=lambda: open_new_window(difficulty_window), width=21)
    button_left.place(relx=0.07, rely=0.03)

    button_right = Button(difficulty_window, text='Уровень 2', bg='salmon4', fg='rosybrown2',
                          font=('Comic Sans MS', 20), command=lambda: open_new_window_2(difficulty_window), width=21)
    button_right.place(relx=0.55, rely=0.03, )

    # Кнопка для возвращения к предыдущему окну
    back_button = Button(difficulty_window, text='Главное меню', bg='lightpink2', fg='salmon4',
                         font=('Comic Sans MS', 20), command=lambda: go_back(difficulty_window), width=21)
    back_button.pack(side='bottom')
    back_button.place(relx=0.5, rely=0.94, anchor=CENTER)

def go_back(window):
    window.destroy()
    root.deiconify()  # Показываем предыдущее окно

def open_new_window(previous_window):
    previous_window.destroy()  # Закрываем предыдущее окно
    new_window = Toplevel()
    new_window.title('Уровень 1') #Уровень1
    new_window.geometry('913x580+300+100')
    new_window.resizable(0, 0)

    new_window.image = PhotoImage(file='экрформа5.png')
    bg_logo = Label(new_window, image=new_window.image)
    bg_logo.place(x=0, y=0, relwidth=1, relheight=1)

    back_to_main_button = Button(new_window, text='Главное меню', bg='salmon4', fg='lightpink2',
                                 font=('Comic Sans MS', 20), command=lambda: go_back_to_main(new_window), width=18)
    back_to_main_button.place(relx=0.18, rely=0.90, anchor=CENTER)


def go_back_to_main(window):
    window.destroy()  # Закрываем текущее окно
    root.deiconify()  # Показываем главное окно

def open_new_window_2(previous_window):
    previous_window.destroy()  # Закрываем предыдущее окно
    new_window_2 = Toplevel()
    new_window_2.title('Уровень 2') #Уровень2
    new_window_2.geometry('913x580+300+100')
    new_window_2.resizable(0, 0)

    new_window_2.image = PhotoImage(file='экрформа3.png')
    bg_logo = Label(new_window_2, image=new_window_2.image)
    bg_logo.place(x=0, y=0, relwidth=1, relheight=1)

    back_to_main_button = Button(new_window_2, text='Главное меню', bg='salmon4', fg='lightpink2',
                                 font=('Comic Sans MS', 20), command=lambda: go_back_to_main(new_window_2), width=18)
    back_to_main_button.place(relx=0.18, rely=0.90, anchor=CENTER)


def go_back_to_main(window):
    window.destroy()  # Закрываем текущее окно
    root.deiconify()  # Показываем главное окно


root = Tk()
root.title('Быки и коровы')
root.geometry('913x580+300+100')

root.image = PhotoImage(file='экрформа1.png')
bg_logo = Label(root, image=root.image)
bg_logo.place(x=0, y=0, relwidth=1, relheight=1)

button_select_level = Button(root, text='Выбор уровня сложности', bg='rosybrown2', fg='salmon4',
                             font=('Comic Sans MS', 20), command=open_difficulty_window)
button_select_level.place(relx=0.5, rely=0.5, anchor=CENTER)

button_exit_game = Button(root, text='Выход из игры', bg='salmon4', fg='rosybrown2', font=('Comic Sans MS', 20),
                          command=exit_game, width=21)
button_exit_game.place(relx=0.5, rely=0.7, anchor=CENTER)

root.resizable(0, 0)

root.mainloop()
