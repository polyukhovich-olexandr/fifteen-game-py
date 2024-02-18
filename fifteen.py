# Імпорт необхідних бібліотек
from random import shuffle
from tkinter import Canvas, Tk

# Задання констант
# Розмір ігрового поля (4x4)
BOARD_SIZE = 4
# Розмір одного блоку у пікселях
SQUARE_SIZE = 80
# Значення порожнього блоку.
# У нашому випадку порожнім буде останній блок
EMPTY_SQUARE = BOARD_SIZE**2
# Головне вікно
root = Tk()
root.title("Pythonicway Fifteen")
# Область для малювання
c = Canvas(
    root, width=BOARD_SIZE * SQUARE_SIZE, height=BOARD_SIZE * SQUARE_SIZE, bg="#808080"
)
c.pack()
