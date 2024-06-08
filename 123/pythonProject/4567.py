from tkinter import *


def open_new_window(previous_window):
    previous_window.destroy()  # Закрываем предыдущее окно
    new_window = Toplevel()
    new_window.title('Уровень 1')  # Уровень1
    new_window.geometry('913x580+300+100')
    new_window.resizable(0, 0)

    new_window.image = PhotoImage(file='экрформа5.png')
    bg_logo = Label(new_window, image=new_window.image)
    bg_logo.place(x=0, y=0, relwidth=1, relheight=1)

    # Генерируем четырехзначное число
    import random
    secret_number = str(random.randint(1000, 9999))
    print(secret_number)  # Для тестирования

    history = []
    move_counter = 1
    remaining_attempts = 10

    def start_game():
        nonlocal move_counter, remaining_attempts
        user_guess = entry_number.get()
        if len(user_guess) != 4 or not user_guess.isdigit():
            result_label.config(text='Пожалуйста, введите четырехзначное число.')
            return

        bulls = 0
        cows = 0

        remaining_attempts -= 1
        attempts_label.config(text=f'Осталось попыток: {remaining_attempts}')

        for i in range(4):
            if user_guess[i] == secret_number[i]:
                bulls += 1
            elif user_guess[i] in secret_number:
                cows += 1

        result_label.config(text='')
        history.append((user_guess, bulls, cows, move_counter))
        move_counter += 1

        update_history_label()

        if remaining_attempts == 0:
            entry_number.config(state='disabled')
            start_game_button.config(state='disabled')

    def update_history_label():
        history_text = ""
        for idx, (guess, bulls, cows, move) in enumerate(history):
            history_label = guess_labels[idx]
            history_label.config(text=f'{guess} ')
            history_label.place(relx=0.48, rely=0.17 + idx * 0.07, anchor=NW)

            move_counter_label = move_counter_labels[idx]
            move_counter_label.config(text=str(move))
            move_counter_label.place(relx=0.39, rely=0.17 + idx * 0.07, anchor=NW)

        # Отображение быков и коров в отдельных метках
        for idx, (guess, bulls, cows, move) in enumerate(history):
            bulls_labels[idx].config(text=str(bulls))
            cows_labels[idx].config(text=str(cows))

    def reset_game():
        nonlocal move_counter, secret_number, history, remaining_attempts
        move_counter = 1
        secret_number = str(random.randint(1000, 9999))
        remaining_attempts = 10
        history.clear()
        result_label.config(text='')
        attempts_label.config(text=f'Осталось попыток: {remaining_attempts}')
        for label in guess_labels + bulls_labels + cows_labels + move_counter_labels:
            label.config(text='')
        entry_number.config(state='normal')
        start_game_button.config(state='normal')

    entry_number = Entry(new_window, font=('Comic Sans MS', 20), width=15)
    entry_number.place(relx=0.17, rely=0.2, anchor=CENTER)

    start_game_button = Button(new_window, text='сделать ход', bg='salmon4', fg='lightpink2',
                               font=('Comic Sans MS', 20), command=start_game, width=18)
    start_game_button.place(relx=0.17, rely=0.30, anchor=CENTER)

    result_label = Label(new_window, text='', font=('Comic Sans MS', 20), bg='snow')
    result_label.place(relx=0.60, rely=0.60, anchor=CENTER)

    history_label = Label(new_window, text='', font=('Comic Sans MS', 16), bg='snow')
    history_label.place(relx=0.40, rely=0.17, anchor=NW)

    attempts_label = Label(new_window, text=f'Осталось попыток: {remaining_attempts}', font=('Comic Sans MS', 16), bg='snow')
    attempts_label.place(relx=0.04, rely=0.05, anchor=NW)

    # Метки для отображения быков и коров
    move_counter_labels = [Label(new_window, text='', font=('Comic Sans MS', 16), bg='snow') for _ in range(10)]
    bulls_labels = [Label(new_window, text='', font=('Comic Sans MS', 16), bg='snow') for _ in range(10)]
    cows_labels = [Label(new_window, text='', font=('Comic Sans MS', 16), bg='snow') for _ in range(10)]
    guess_labels = [Label(new_window, text='', font=('Comic Sans MS', 16), bg='snow') for _ in range(10)]

    for idx in range(10):
        move_counter_labels[idx].place(relx=0.39, rely=0.17 + idx * 0.07, anchor=NW)
        bulls_labels[idx].place(relx=0.67, rely=0.2 + idx * 0.07, anchor=CENTER)
        cows_labels[idx].place(relx=0.87, rely=0.2 + idx * 0.07, anchor=CENTER)

    def go_back_to_main(window):
        window.destroy()
        # Добавьте здесь код для перехода на главное меню

    back_to_main_button = Button(new_window, text='Главное меню', bg='salmon4', fg='lightpink2',
                                 font=('Comic Sans MS', 20), command=lambda: go_back_to_main(new_window), width=18)
    back_to_main_button.place(relx=0.17, rely=0.90, anchor=CENTER)

    reset_button = Button(new_window, text='Начать сначала', bg='salmon4', fg='lightpink2',
                          font=('Comic Sans MS', 20), command=reset_game, width=18)
    reset_button.place(relx=0.17, rely=0.76, anchor=CENTER)


# Пример использования
root = Tk()
open_new_window(root)
root.mainloop()