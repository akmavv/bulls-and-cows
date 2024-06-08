from tkinter import *
import random


def exit_game():
    root.destroy()


def open_difficulty_window():
    root.withdraw()
    difficulty_window = Toplevel()
    difficulty_window.title('Выбор уровня сложности')
    difficulty_window.geometry('913x580+300+100')
    difficulty_window.resizable(0, 0)

    difficulty_window.image = PhotoImage(file='back2.png')
    bg_logo = Label(difficulty_window, image=difficulty_window.image)
    bg_logo.place(x=0, y=0, relwidth=1, relheight=1)

    button_left = Button(difficulty_window, text='Уровень 1', bg='rosybrown2', fg='salmon4',
                         font=('Comic Sans MS', 20), command=lambda: open_new_window(difficulty_window), width=21)
    button_left.place(relx=0.07, rely=0.03)

    button_right = Button(difficulty_window, text='Уровень 2', bg='salmon4', fg='rosybrown2',
                          font=('Comic Sans MS', 20), command=lambda: open_new_window_2(difficulty_window), width=21)
    button_right.place(relx=0.55, rely=0.03, )

    back_button = Button(difficulty_window, text='Главное меню', bg='lightpink2', fg='salmon4',
                         font=('Comic Sans MS', 20), command=lambda: go_back(difficulty_window), width=21)
    back_button.pack(side='bottom')
    back_button.place(relx=0.5, rely=0.94, anchor=CENTER)


def go_back(window):
    window.destroy()
    root.deiconify()


def open_new_window(previous_window):
    previous_window.destroy()
    new_window = Toplevel()
    new_window.title('Уровень 1')
    new_window.geometry('913x580+300+100')
    new_window.resizable(0, 0)

    new_window.image = PhotoImage(file='back5.png')
    bg_logo = Label(new_window, image=new_window.image)
    bg_logo.place(x=0, y=0, relwidth=1, relheight=1)

    def generate_secret_number():
        number_set = set('0123456789')
        first_digit = str(random.choice([i for i in range(1, 10)]))
        number_set.remove(first_digit)
        secret_number = first_digit
        for i in range(3):
            digit = random.choice(list(number_set))
            number_set.remove(digit)
            secret_number += digit
        return secret_number

    secret_number = generate_secret_number()

    history = []
    move_counter = 1
    remaining_attempts = 10

    def check_input_number(number):
        if len(number) != 4 or not number.isdigit():
            show_error_window("Пожалуйста, введите четырехзначное число.")
            return False
        if number.startswith('0'):
            show_error_window("Число не должно начинаться с нуля.")
            return False
        if len(set(number)) < 4:
            show_error_window("Цифры в числе не должны повторяться.")
            return False
        return True

    def start_game():
        nonlocal move_counter, remaining_attempts
        user_guess = entry_number.get()
        if not check_input_number(user_guess):
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

        if user_guess == secret_number:
            show_winning_number()
            entry_number.config(state='disabled')
            start_game_button.config(state='disabled')
        elif remaining_attempts == 0:
            entry_number.config(state='disabled')
            start_game_button.config(state='disabled')
            show_secret_number()

    def update_history_label():
        for idx, (guess, bulls, cows, move) in enumerate(history):
            history_label = guess_labels[idx]
            history_label.config(text=f'{guess} ')
            history_label.place(relx=0.48, rely=0.17 + idx * 0.07, anchor=NW)

            move_counter_label = move_counter_labels[idx]
            move_counter_label.config(text=str(move))
            move_counter_label.place(relx=0.39, rely=0.17 + idx * 0.07, anchor=NW)

        for idx, (guess, bulls, cows, move) in enumerate(history):
            bulls_labels[idx].config(text=str(bulls))
            cows_labels[idx].config(text=str(cows))

    def show_error_window(message):
        error_window = Toplevel()
        error_window.title('Ошибка')
        error_window.geometry('400x100+550+280')
        error_window.resizable(0, 0)

        error_label = Label(error_window, text=message, font=('Arial', 14))
        error_label.pack(pady=20)

    def reset_game():
        nonlocal move_counter, secret_number, history, remaining_attempts
        move_counter = 1
        secret_number = generate_secret_number()
        remaining_attempts = 10
        history.clear()
        result_label.config(text='')
        attempts_label.config(text=f'Осталось попыток: {remaining_attempts}')
        for label in guess_labels + bulls_labels + cows_labels + move_counter_labels:
            label.config(text='')
        entry_number.config(state='normal')
        start_game_button.config(state='normal')

    def show_secret_number():
        lost_window = Toplevel()
        lost_window.title('Вы проиграли!')
        lost_window.geometry('400x100+550+280')
        lost_window.resizable(0, 0)

        lost_label = Label(lost_window, text=f'Вы проиграли! Загаданное число: {secret_number}', font=('Arial', 14))
        lost_label.pack(pady=20)

    def show_winning_number():
        win_window = Toplevel()
        win_window.title('Победа!')
        win_window.geometry('400x100+550+280')
        win_window.resizable(0, 0)

        win_label = Label(win_window, text=f'Вы победили! Загаданное число: {secret_number}', font=('Arial', 14))
        win_label.pack(pady=20)

    entry_number = Entry(new_window, font=('Comic Sans MS', 20), width=15)
    entry_number.place(relx=0.17, rely=0.2, anchor=CENTER)

    start_game_button = Button(new_window, text='сделать ход', bg='salmon4', fg='lightpink2',
                               font=('Comic Sans MS', 20), command=start_game, width=18)
    start_game_button.place(relx=0.17, rely=0.30, anchor=CENTER)

    result_label = Label(new_window, text='', font=('Comic Sans MS', 20), bg='snow')
    result_label.place(relx=0.60, rely=0.60, anchor=CENTER)

    history_label = Label(new_window, text='', font=('Comic Sans MS', 16), bg='snow')
    history_label.place(relx=0.40, rely=0.17, anchor=NW)

    attempts_label = Label(new_window, text=f'Осталось попыток: {remaining_attempts}', font=('Comic Sans MS', 16),
                           bg='snow')
    attempts_label.place(relx=0.02, rely=0.02, anchor=NW)

    move_counter_labels = [Label(new_window, text='', font=('Comic Sans MS', 16), bg='snow') for _ in range(10)]
    bulls_labels = [Label(new_window, text='', font=('Comic Sans MS', 16), bg='snow') for _ in range(10)]
    cows_labels = [Label(new_window, text='', font=('Comic Sans MS', 16), bg='snow') for _ in range(10)]
    guess_labels = [Label(new_window, text='', font=('Comic Sans MS', 16), bg='snow') for _ in range(10)]

    for idx in range(10):
        move_counter_labels[idx].place(relx=0.39, rely=0.17 + idx * 0.07, anchor=NW)
        bulls_labels[idx].place(relx=0.67, rely=0.2 + idx * 0.07, anchor=CENTER)
        cows_labels[idx].place(relx=0.87, rely=0.2 + idx * 0.07, anchor=CENTER)

    back_to_main_button = Button(new_window, text='Главное меню', bg='salmon4', fg='lightpink2',
                                 font=('Comic Sans MS', 20), command=lambda: go_back_to_main(new_window), width=18)
    back_to_main_button.place(relx=0.17, rely=0.90, anchor=CENTER)

    reset_button = Button(new_window, text='Начать сначала', bg='lightpink2', fg='salmon4',
                          font=('Comic Sans MS', 20), command=reset_game, width=18)
    reset_button.place(relx=0.17, rely=0.76, anchor=CENTER)


def go_back_to_main(window):
    window.destroy()
    root.deiconify()


def open_new_window_2(previous_window):
    previous_window.destroy()
    new_window_2 = Toplevel()
    new_window_2.title('Уровень 2')
    new_window_2.geometry('913x580+300+100')
    new_window_2.resizable(0, 0)

    new_window_2.image = PhotoImage(file='back5.png')
    bg_logo = Label(new_window_2, image=new_window_2.image)
    bg_logo.place(x=0, y=0, relwidth=1, relheight=1)

    def generate_secret_number():
        number_set = set('0123456789')
        first_digit = str(random.choice([i for i in range(1, 10)]))  # Число не начинается с нуля
        number_set.remove(first_digit)
        secret_number = first_digit
        for i in range(4):
            digit = random.choice(list(number_set))
            number_set.remove(digit)
            secret_number += digit
        return secret_number

    secret_number = generate_secret_number()

    history = []
    move_counter = 1
    remaining_attempts = 15

    def check_input_number(number):
        if len(number) != 5 or not number.isdigit():
            show_error_window("Пожалуйста, введите пятизначное число.")
            return False
        if number.startswith('0'):
            show_error_window("Число должно начинаться не с нуля.")
            return False
        if len(set(number)) < 5:
            show_error_window("Цифры в числе не должны повторяться.")
            return False
        return True

    def start_game():
        nonlocal move_counter, remaining_attempts
        user_guess = entry_number.get()
        if not check_input_number(user_guess):
            return

        bulls = 0
        cows = 0

        remaining_attempts -= 1
        attempts_label.config(text=f'Осталось попыток: {remaining_attempts}')

        for i in range(5):
            if user_guess[i] == secret_number[i]:
                bulls += 1
            elif user_guess[i] in secret_number:
                cows += 1

        result_label.config(text='')
        history.append((user_guess, bulls, cows, move_counter))
        move_counter += 1

        update_history_label()

        if user_guess == secret_number:
            show_winning_number()
            entry_number.config(state='disabled')
            start_game_button.config(state='disabled')
        elif remaining_attempts == 0:
            entry_number.config(state='disabled')
            start_game_button.config(state='disabled')
            show_secret_number()

    def update_history_label():
        for idx, (guess, bulls, cows, move) in enumerate(history):
            history_label = guess_labels[idx]
            history_label.config(text=f'{guess} ')
            history_label.place(relx=0.48, rely=0.17 + idx * 0.05, anchor=NW)

            move_counter_label = move_counter_labels[idx]
            move_counter_label.config(text=str(move))
            move_counter_label.place(relx=0.39, rely=0.17 + idx * 0.05, anchor=NW)

        for idx, (guess, bulls, cows, move) in enumerate(history):
            bulls_labels[idx].config(text=str(bulls))
            cows_labels[idx].config(text=str(cows))

    def show_error_window(message):
        error_window = Toplevel()
        error_window.title('Ошибка')
        error_window.geometry('400x100+550+280')
        error_window.resizable(0, 0)

        error_label = Label(error_window, text=message, font=('Arial', 14))
        error_label.pack(pady=20)

    def reset_game():
        nonlocal move_counter, secret_number, history, remaining_attempts
        move_counter = 1
        secret_number = generate_secret_number()
        remaining_attempts = 15
        history.clear()
        result_label.config(text='')
        attempts_label.config(text=f'Осталось попыток: {remaining_attempts}')
        for label in guess_labels + bulls_labels + cows_labels + move_counter_labels:
            label.config(text='')
        entry_number.config(state='normal')
        start_game_button.config(state='normal')

    def show_secret_number():
        lost_window = Toplevel()
        lost_window.title('Вы проиграли!')
        lost_window.geometry('400x100+550+280')
        lost_window.resizable(0, 0)

        lost_label = Label(lost_window, text=f'Вы проиграли! Загаданное число: {secret_number}', font=('Arial', 14))
        lost_label.pack(pady=20)

    def show_winning_number():
        win_window = Toplevel()
        win_window.title('Победа!')
        win_window.geometry('400x100+550+280')
        win_window.resizable(0, 0)

        win_label = Label(win_window, text=f'Вы победили! Загаданное число: {secret_number}', font=('Arial', 14))
        win_label.pack(pady=20)

    entry_number = Entry(new_window_2, font=('Comic Sans MS', 20), width=15)
    entry_number.place(relx=0.17, rely=0.2, anchor=CENTER)

    start_game_button = Button(new_window_2, text='сделать ход', bg='salmon4', fg='lightpink2',
                               font=('Comic Sans MS', 20), command=start_game, width=18)
    start_game_button.place(relx=0.17, rely=0.30, anchor=CENTER)

    result_label = Label(new_window_2, text='', font=('Comic Sans MS', 20), bg='snow')
    result_label.place(relx=0.60, rely=0.60, anchor=CENTER)

    history_label = Label(new_window_2, text='', font=('Comic Sans MS', 16), bg='snow')
    history_label.place(relx=0.40, rely=0.17, anchor=NW)

    attempts_label = Label(new_window_2, text=f'Осталось попыток: {remaining_attempts}', font=('Comic Sans MS', 16),
                           bg='snow')
    attempts_label.place(relx=0.02, rely=0.02, anchor=NW)

    move_counter_labels = [Label(new_window_2, text='', font=('Comic Sans MS', 16), bg='snow') for _ in range(15)]
    bulls_labels = [Label(new_window_2, text='', font=('Comic Sans MS', 16), bg='snow') for _ in range(15)]
    cows_labels = [Label(new_window_2, text='', font=('Comic Sans MS', 16), bg='snow') for _ in range(15)]
    guess_labels = [Label(new_window_2, text='', font=('Comic Sans MS', 16), bg='snow') for _ in range(15)]

    for idx in range(15):
        move_counter_labels[idx].place(relx=0.39, rely=0.17 + idx * 0.05, anchor=NW)
        bulls_labels[idx].place(relx=0.66, rely=0.17 + idx * 0.05, anchor=NW)
        cows_labels[idx].place(relx=0.86, rely=0.17 + idx * 0.05, anchor=NW)

    back_to_main_button = Button(new_window_2, text='Главное меню', bg='salmon4', fg='lightpink2',
                                 font=('Comic Sans MS', 20), command=lambda: go_back_to_main(new_window_2), width=18)
    back_to_main_button.place(relx=0.17, rely=0.90, anchor=CENTER)

    reset_button = Button(new_window_2, text='Начать сначала', bg='lightpink2', fg='salmon4',
                          font=('Comic Sans MS', 20), command=reset_game, width=18)
    reset_button.place(relx=0.17, rely=0.76, anchor=CENTER)


def go_back_to_main(window):
    window.destroy()
    root.deiconify()


root = Tk()
root.title('Главное меню')
root.geometry('913x580+300+100')

root.image = PhotoImage(file='123/back1.png')
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
