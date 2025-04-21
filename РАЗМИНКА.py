from tkinter import *
from PIL import Image, ImageTk
import pygame
import random
import os
from tkinter import ttk

pygame.init()
pygame.mixer.init()
root = Tk()
root.title("Игра")
root.geometry("1980x1080")
root.resizable()

from pygame import mixer

word_dict = {
    'but': 'но',
    'if': 'если',
    'never': 'никогда',
    'for': 'для',
    'need': 'нужно'
}

hard = list(word_dict.keys())
current_word = None

mixer.init()
mixer.music.load('C418-Subwoofer-Lullaby.wav')
mixer.music.play()

root_image = PhotoImage(file='1667338567_4-zefirka-club-p-temnii-fon-mainkraft-4.png')
bg_logo = Label(root, image=root_image)
bg_logo.grid(row=0, column=0)

result_label = Label(root, font='Arial 25')
result_label.place(relx=0.5, rely=0.7, anchor=CENTER)

# Загрузка изображения для проигрыша
try:
    lose_image = PhotoImage(file='Slider-Minecraft-1980x1080-1-scaled.png')
    lose_label = Label(root, image=lose_image)
    lose_label.place(relx=0.5, rely=0.4, anchor=CENTER)
    lose_label.place_forget()
except:
    print("Не удалось загрузить изображение проигрыша")

def clickhard():
    global current_word
    current_word = random.choice(hard)
    label1.config(text=current_word)
    entry.delete(0, END)
    result_label.config(text="")
    lose_label.place_forget()
    btn_restart.place_forget()

def check_translation(event=None):
    user_translation = entry.get().strip().lower()
    if current_word and user_translation:
        correct_translation = word_dict[current_word].lower()
        if user_translation == correct_translation:
            result_label.config(text="Да", fg="green")
        else:
            result_label.config(text="Нет", fg="red")
            lose_label.place(relx=0.5, rely=0.4, anchor=CENTER)
            btn_restart.place(relx=0.5, rely=0.8, anchor=CENTER)

def restart_game():
    clickhard()

# Создаем кнопку "Начать"
btn2 = Button(root, text='Начать', height=3, width=40, command=clickhard, foreground="#FFFFFF", background="#7D9C6A")
btn2.place(relx=0.5, rely=0.5, anchor=CENTER)

# Создаем поле для ввода
entry = Entry(root, font='Arial 25')
entry.place(relx=0.5, rely=0.6, anchor=CENTER)
entry.bind('<Return>', check_translation)

# Кнопка для проверки перевода
check_button = Button(root, text="Проверить", command=check_translation, height=2, width=15)
check_button.place(relx=0.5, rely=0.65, anchor=CENTER)

# Кнопка "Заново"
btn_restart = Button(root, text='Заново', height=3, width=40, command=restart_game, foreground="#FFFFFF", background="#7D9C6A")
btn_restart.place(relx=0.5, rely=0.8, anchor=CENTER)
btn_restart.place_forget()

label1 = Label(root, font='Arial 25')
label1.place(x=900, y=380)

root.mainloop()