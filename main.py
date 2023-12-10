import random
import time
import tkinter.messagebox
import customtkinter
from tkinter import *
from packaging import version
import threading
from list_color import colors
import default_value

balance = default_value.balance
all_game = default_value.all_game
win_game = default_value.win_game
lose_game = default_value.lose_game
cell_count = default_value.cell_count
history_count = default_value.history_count
rez = default_value.rez
speed_roulette = default_value.speed_roulette
time_roulette = default_value.time_roulette


# Функция умножения поля ставки в 2 раза


def multiply():
    a = ent_rate.get()
    a = int(a)
    ent_rate.delete(0, END)
    ent_rate.insert(0, a * 2)


# Функция деления поля ставки в 2 раза
def split():
    a = ent_rate.get()
    a = int(a)
    ent_rate.delete(0, END)
    ent_rate.insert(0, a // 2)


# Функция всей суммы в поле ставки
def all_in():
    ent_rate.delete(0, END)
    ent_rate.insert(0, balance)


# Проверка нажатия кнопки black
def black_game():
    global balance
    if balance < int(ent_rate.get()):
        tkinter.messagebox.showerror('Ошибка', 'На балансе не хватает денег!')
        return
    else:
        if int(ent_rate.get()) == 0:
            tkinter.messagebox.showerror('Ошибка', 'Минимальная ставка: 1')
            return
        else:
            ent_rate.configure(state=DISABLED)
            label_result.configure(text='')
            balance -= int(ent_rate.get())
            label_balance.configure(text=f'Баланс: {balance}')
            global color_switch
            color_switch = 'black'
            black_lab.configure(text=f'ставка: {ent_rate.get()}')
            green_btn.configure(state=DISABLED)
            red_btn.configure(state=DISABLED)
            black_btn.configure(state=DISABLED)
            blue_btn.configure(state=DISABLED)
            yellow_btn.configure(state=DISABLED)
            th_start = threading.Thread(target=game_logic)
            th_start.start()


# Проверка нажатия кнопки red
def red_game():
    global balance
    if balance < int(ent_rate.get()):
        tkinter.messagebox.showerror('Ошибка', 'На балансе не хватает денег!')
        return
    else:
        if int(ent_rate.get()) == 0:
            tkinter.messagebox.showerror('Ошибка', 'Минимальная ставка: 1')
            return
        else:
            ent_rate.configure(state=DISABLED)
            label_result.configure(text='')
            balance -= int(ent_rate.get())
            label_balance.configure(text=f'Баланс: {balance}')
            global color_switch
            color_switch = 'red'
            red_lab.configure(text=f'ставка: {ent_rate.get()}')
            green_btn.configure(state=DISABLED)
            red_btn.configure(state=DISABLED)
            black_btn.configure(state=DISABLED)
            blue_btn.configure(state=DISABLED)
            yellow_btn.configure(state=DISABLED)
            th_start = threading.Thread(target=game_logic)
            th_start.start()


# Проверка нажатия кнопки blue
def blue_game():
    global balance
    if balance < int(ent_rate.get()):
        tkinter.messagebox.showerror('Ошибка', 'На балансе не хватает денег!')
        return
    else:
        if int(ent_rate.get()) == 0:
            tkinter.messagebox.showerror('Ошибка', 'Минимальная ставка: 1')
            return
        else:
            ent_rate.configure(state=DISABLED)
            label_result.configure(text='')
            balance -= int(ent_rate.get())
            label_balance.configure(text=f'Баланс: {balance}')
            global color_switch
            color_switch = 'blue'
            blue_lab.configure(text=f'ставка: {ent_rate.get()}')
            red_btn.configure(state=DISABLED)
            black_btn.configure(state=DISABLED)
            green_btn.configure(state=DISABLED)
            blue_btn.configure(state=DISABLED)
            yellow_btn.configure(state=DISABLED)
            th_start = threading.Thread(target=game_logic)
            th_start.start()


# Проверка нажатия кнопки green
def green_game():
    global balance
    if balance < int(ent_rate.get()):
        tkinter.messagebox.showerror('Ошибка', 'На балансе не хватает денег!')
        return
    else:
        if int(ent_rate.get()) == 0:
            tkinter.messagebox.showerror('Ошибка', 'Минимальная ставка: 1')
            return
        else:
            ent_rate.configure(state=DISABLED)
            label_result.configure(text='')
            balance -= int(ent_rate.get())
            label_balance.configure(text=f'Баланс: {balance}')
            global color_switch
            color_switch = 'green'
            green_lab.configure(text=f'ставка: {ent_rate.get()}')
            red_btn.configure(state=DISABLED)
            black_btn.configure(state=DISABLED)
            green_btn.configure(state=DISABLED)
            blue_btn.configure(state=DISABLED)
            yellow_btn.configure(state=DISABLED)
            th_start = threading.Thread(target=game_logic)
            th_start.start()


# Проверка нажатия кнопки yellow
def yellow_game():
    global balance
    if balance < int(ent_rate.get()):
        tkinter.messagebox.showerror('Ошибка', 'На балансе не хватает денег!')
        return
    else:
        if int(ent_rate.get()) == 0:
            tkinter.messagebox.showerror('Ошибка', 'Минимальная ставка: 1')
            return
        else:
            ent_rate.configure(state=DISABLED)
            label_result.configure(text='')
            balance -= int(ent_rate.get())
            label_balance.configure(text=f'Баланс: {balance}')
            global color_switch
            color_switch = 'yellow'
            yellow_lab.configure(text=f'ставка: {ent_rate.get()}')
            red_btn.configure(state=DISABLED)
            black_btn.configure(state=DISABLED)
            green_btn.configure(state=DISABLED)
            blue_btn.configure(state=DISABLED)
            yellow_btn.configure(state=DISABLED)
            game_logic()


# Главный цикл игры
def game_logic():
    global all_game, win_game, lose_game, time_roulette, balance, speed_roulette
    all_game += 1
    label_all_game.configure(text=f'Игр сыграно: {all_game}')
    black_win = int(ent_rate.get()) * 2
    red_win = int(ent_rate.get()) * 3
    blue_win = int(ent_rate.get()) * 6
    green_win = int(ent_rate.get()) * 25
    yellow_win = int(ent_rate.get()) * 50

    random.shuffle(colors)
    color_canvas = colors

    temp = time_roulette
    color = random.choice(color_canvas)

    if var.get() == 0:
        speed_roulette = 1
    elif var.get() == 1:
        speed_roulette = 0.5
    elif var.get() == 2:
        speed_roulette = 0.25

    while temp > -1:
        color = random.choice(color_canvas)
        label_timer.configure(text=temp)
        globals()['cell%s' % temp] = customtkinter.CTkCanvas(frame_roulette, width=50, height=50,
                                                             background=color,
                                                             highlightthickness=1)
        globals()['cell%s' % temp].pack(side='left', padx=(0, 3))
        switch_game.update()
        time.sleep(speed_roulette)
        temp -= 1

    global history_count, rez, cell_count
    if color == color_switch:
        if color == 'black':
            balance = balance + black_win
            label_result.configure(text=f'Вы выйграли! +{black_win}')
            label_balance.configure(text=f'Баланс: {balance}')

        if color == 'red':
            balance = balance + red_win
            label_result.configure(text=f'Вы выйграли! +{red_win}')
            label_balance.configure(text=f'Баланс: {balance}')

        if color == 'blue':
            balance = balance + blue_win
            label_result.configure(text=f'Вы выйграли! +{blue_win}')
            label_balance.configure(text=f'Баланс: {balance}')

        if color == 'green':
            balance = balance + green_win
            label_result.configure(text=f'Вы выйграли! +{green_win}')
            label_balance.configure(text=f'Баланс: {balance}')

        if color == 'yellow':
            balance = balance + yellow_win
            label_result.configure(text=f'Вы выйграли! +{yellow_win}')
            label_balance.configure(text=f'Баланс: {balance}')

        if cell_count >= 15:
            if color == 'yellow':
                globals()['cell_history%s' % rez].destroy()
                rez += 1
                globals()['cell_history%s' % history_count] = customtkinter.CTkCanvas(frame_history, width=35,
                                                                                      height=35,
                                                                                      background=color)
                globals()['cell_history%s' % history_count].pack(side='left')
                label_res = customtkinter.CTkLabel(globals()['cell_history%s' % history_count], text='W',
                                                   text_color='black')
                label_res.place(relx=0.5, rely=0.5, anchor=CENTER)
                history_count += 1
            else:
                globals()['cell_history%s' % rez].destroy()
                rez += 1
                globals()['cell_history%s' % history_count] = customtkinter.CTkCanvas(frame_history, width=35,
                                                                                      height=35,
                                                                                      background=color)
                globals()['cell_history%s' % history_count].pack(side='left')
                label_res = customtkinter.CTkLabel(globals()['cell_history%s' % history_count], text='W',
                                                   text_color='white')
                label_res.place(relx=0.5, rely=0.5, anchor=CENTER)
                history_count += 1

        else:
            if color == 'yellow':
                globals()['cell_history%s' % history_count] = customtkinter.CTkCanvas(frame_history, width=35,
                                                                                      height=35,
                                                                                      background=color)
                globals()['cell_history%s' % history_count].pack(side='left')
                label_res = customtkinter.CTkLabel(globals()['cell_history%s' % history_count], text='W',
                                                   text_color='black')
                label_res.place(relx=0.5, rely=0.5, anchor=CENTER)
                cell_count += 1
                history_count += 1
            else:
                globals()['cell_history%s' % history_count] = customtkinter.CTkCanvas(frame_history, width=35,
                                                                                      height=35,
                                                                                      background=color)
                globals()['cell_history%s' % history_count].pack(side='left')
                label_res = customtkinter.CTkLabel(globals()['cell_history%s' % history_count], text='W',
                                                   text_color='white')
                label_res.place(relx=0.5, rely=0.5, anchor=CENTER)
                cell_count += 1
                history_count += 1

        red_btn.configure(state=NORMAL)
        green_btn.configure(state=NORMAL)
        black_btn.configure(state=NORMAL)
        blue_btn.configure(state=NORMAL)
        yellow_btn.configure(state=NORMAL)
        ent_rate.configure(state=NORMAL)

        red_lab.configure(text='cтавка: 0')
        green_lab.configure(text='cтавка: 0')
        black_lab.configure(text='cтавка: 0')
        blue_lab.configure(text='cтавка: 0')
        yellow_lab.configure(text='cтавка: 0')
        win_game += 1
        label_win_game.configure(text=f'Игр выиграно: {win_game}')

        for x in range(0, 6):
            globals()['cell%s' % x].destroy()

    else:
        label_result.configure(text='Вы проиграли!')
        red_btn.configure(state=NORMAL)
        green_btn.configure(state=NORMAL)
        black_btn.configure(state=NORMAL)
        blue_btn.configure(state=NORMAL)
        yellow_btn.configure(state=NORMAL)

        red_lab.configure(text='0')
        green_lab.configure(text='0')
        black_lab.configure(text='0')
        blue_lab.configure(text='0')
        yellow_lab.configure(text='0')

        lose_game += 1
        label_lose_game.configure(text=f'Игр проиграно: {lose_game}')

        for x in range(0, 6):
            globals()['cell%s' % x].destroy()

        ent_rate.configure(state=NORMAL)

        if cell_count >= 15:
            if color == 'yellow':
                globals()['cell_history%s' % rez].destroy()
                rez += 1
                globals()['cell_history%s' % history_count] = customtkinter.CTkCanvas(frame_history, width=35,
                                                                                      height=35,
                                                                                      background=color)
                globals()['cell_history%s' % history_count].pack(side='left')
                label_res = customtkinter.CTkLabel(globals()['cell_history%s' % history_count], text='L',
                                                   text_color='black')
                label_res.place(relx=0.5, rely=0.5, anchor=CENTER)
                history_count += 1
            else:
                globals()['cell_history%s' % rez].destroy()
                rez += 1
                globals()['cell_history%s' % history_count] = customtkinter.CTkCanvas(frame_history, width=35,
                                                                                      height=35,
                                                                                      background=color)
                globals()['cell_history%s' % history_count].pack(side='left')
                label_res = customtkinter.CTkLabel(globals()['cell_history%s' % history_count], text='L',
                                                   text_color='white')
                label_res.place(relx=0.5, rely=0.5, anchor=CENTER)
                history_count += 1

        else:
            if color == 'yellow':
                globals()['cell_history%s' % history_count] = customtkinter.CTkCanvas(frame_history, width=35,
                                                                                      height=35,
                                                                                      background=color)
                globals()['cell_history%s' % history_count].pack(side='left')
                label_res = customtkinter.CTkLabel(globals()['cell_history%s' % history_count], text='L',
                                                   text_color='black')
                label_res.place(relx=0.5, rely=0.5, anchor=CENTER)
                cell_count += 1
                history_count += 1
            else:
                globals()['cell_history%s' % history_count] = customtkinter.CTkCanvas(frame_history, width=35,
                                                                                      height=35,
                                                                                      background=color)
                globals()['cell_history%s' % history_count].pack(side='left')
                label_res = customtkinter.CTkLabel(globals()['cell_history%s' % history_count], text='L',
                                                   text_color='white')
                label_res.place(relx=0.5, rely=0.5, anchor=CENTER)
                cell_count += 1
                history_count += 1


# Функция добавления денег на баланс
def add_balance():
    global balance
    if balance > 1:
        # tkinter.messagebox.showerror('Ошибка', 'Бесплатный бонус доступен, когда баланс равен 0')
        return
    else:
        balance_random = random.randint(100, 3000)
        balance = balance_random
        label_balance.configure(text=f'Баланс: {balance}')
        # tkinter.messagebox.showinfo('Успешно', f'Вам зачислено: {balance_random}')


# Создание окна
def roulette_win():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    global switch_game, label_all_game, label_win_game, label_lose_game, label_balance, btn_add_balance, frame_rate
    global label_rate, ent_rate, font_rate, split_btn, multiply_btn, all_in_btn, frame_color, black_btn, red_btn
    global blue_btn, green_btn, yellow_btn, black_lab, red_lab, blue_lab, green_lab, yellow_lab, frame_history
    global label_result, var, label_timer, frame_roulette

    switch_game = customtkinter.CTk()
    font_rate = customtkinter.CTkFont(family='Arial', size=16, weight='bold')

    switch_game.title('Play2x')
    switch_game.resizable(False, False)
    switch_game.geometry('585x485+700+300')

    label_all_game = customtkinter.CTkLabel(switch_game, text=f'Игр сыграно: {all_game}')
    label_all_game.place(x=10, y=5)

    label_win_game = customtkinter.CTkLabel(switch_game, text=f'Игр выиграно: {win_game}')
    label_win_game.place(x=10, y=25)

    label_lose_game = customtkinter.CTkLabel(switch_game, text=f'Игр проиграно: {lose_game}')
    label_lose_game.place(x=10, y=45)

    label_balance = customtkinter.CTkLabel(switch_game, text=f'Баланс: {balance}', font=font_rate)
    label_balance.place(x=430, y=5)
    btn_add_balance = customtkinter.CTkButton(switch_game, text='+',
                                              font=font_rate, width=20, height=20, command=add_balance)
    btn_add_balance.place(x=400, y=5)

    frame_rate = customtkinter.CTkFrame(switch_game)
    frame_rate.pack(side='top')

    label_rate = customtkinter.CTkLabel(frame_rate, text='Ставка', font=font_rate)
    label_rate.grid(row=0, columnspan=4)

    ent_rate = customtkinter.CTkEntry(frame_rate, width=80, font=font_rate)
    ent_rate.grid(row=1, column=0, padx=(2, 0))
    ent_rate.insert(0, 100)

    split_btn = customtkinter.CTkButton(frame_rate, text='/2', width=30, font=font_rate, command=split)
    split_btn.grid(row=1, column=1, padx=(2, 0))

    multiply_btn = customtkinter.CTkButton(frame_rate, text='x2', width=20, font=font_rate, command=multiply)
    multiply_btn.grid(row=1, column=2, padx=(2, 0))

    all_in_btn = customtkinter.CTkButton(frame_rate, text='all in', width=20, font=font_rate, command=all_in)
    all_in_btn.grid(row=1, column=3, padx=(2, 0))

    frame_color = customtkinter.CTkFrame(switch_game)
    frame_color.pack(pady=20)

    # Black config
    black_btn = customtkinter.CTkButton(frame_color, text='x2',
                                        font=font_rate, fg_color='black', width=110, command=black_game)
    black_btn.grid(row=0, column=0, padx=(5, 0))
    black_lab = customtkinter.CTkLabel(frame_color, text='ставка: 0')
    black_lab.grid(row=1, column=0)

    # Red config
    red_btn = customtkinter.CTkButton(frame_color, text='x3',
                                      font=font_rate, fg_color='red', width=110, command=red_game)
    red_btn.grid(row=0, column=1, padx=(5, 0))
    red_lab = customtkinter.CTkLabel(frame_color, text='ставка: 0')
    red_lab.grid(row=1, column=1)

    # Blue config
    blue_btn = customtkinter.CTkButton(frame_color, text='x6',
                                       font=font_rate, fg_color='blue', width=110, command=blue_game)
    blue_btn.grid(row=0, column=2, padx=(5, 0))
    blue_lab = customtkinter.CTkLabel(frame_color, text='ставка: 0')
    blue_lab.grid(row=1, column=2)

    # Green config
    green_btn = customtkinter.CTkButton(frame_color, text='x25',
                                        font=font_rate, fg_color='green', width=110, command=green_game)
    green_btn.grid(row=0, column=3, padx=(5, 0))
    green_lab = customtkinter.CTkLabel(frame_color, text='ставка: 0')
    green_lab.grid(row=1, column=3)

    # Yellow config
    yellow_btn = customtkinter.CTkButton(frame_color, text='x50',
                                         font=font_rate, fg_color='yellow', width=110, command=yellow_game,
                                         text_color='black')
    yellow_btn.grid(row=0, column=4, padx=(5, 5))
    yellow_lab = customtkinter.CTkLabel(frame_color, text='ставка: 0')
    yellow_lab.grid(row=1, column=4)

    frame_game = customtkinter.CTkFrame(switch_game)
    frame_game.pack(fill=X)

    label_timer = customtkinter.CTkLabel(frame_game, text='', font=font_rate)
    label_timer.pack()

    label_result = customtkinter.CTkLabel(frame_game, text='', font=font_rate)
    label_result.pack()

    label_win_cell = customtkinter.CTkLabel(frame_game, text='↓', font=font_rate)
    label_win_cell.pack()

    frame_roulette = customtkinter.CTkFrame(switch_game, height=50)
    frame_roulette.pack(fill=X)

    frame_history = customtkinter.CTkFrame(switch_game, width=200)
    frame_history.pack(fill=X)

    label_history = customtkinter.CTkLabel(frame_history, text='История', font=font_rate)
    label_history.pack()

    frame_bottom = customtkinter.CTkFrame(switch_game, height=130)
    frame_bottom.pack(fill=X)

    label_speed = customtkinter.CTkLabel(frame_bottom, text='Скорость игры', font=font_rate)
    label_speed.place(x=10, y=10)

    var = IntVar()
    var.set(0)
    speed_default = customtkinter.CTkRadioButton(frame_bottom, text='Стандарт', variable=var, value=0)
    speed_default.place(x=10, y=40)

    speed_fast = customtkinter.CTkRadioButton(frame_bottom, text='Быстро', variable=var, value=1)
    speed_fast.place(x=10, y=70)

    speed_very_fast = customtkinter.CTkRadioButton(frame_bottom, text='Очень быстро', variable=var, value=2)
    speed_very_fast.place(x=10, y=100)

    switch_game.mainloop()


roulette_win()

