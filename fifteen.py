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

# Створюємо список блоків
board = list(range(1, EMPTY_SQUARE + 1))
# Список з яким ми порівнюватимемо результат. В даному випадку це
# просто відсортований список, але при бажанні можна придумати щось інше
correct_board = board[:]
# перемішуємо блоки
shuffle(board)


def draw_board():
    # Прибираємо все, що  нарисоване в області для малювання
    c.delete("all")
    # Наша задача згрупувати п’ятнашки зі списку у квадрат
    # розміром  BOARD_SIZE x BOARD_SIZE
    # i та j будуть координатами для кожної окремої п’ятнашки
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            # Отримуємо значення для його малювання на квадраті
            index = str(board[BOARD_SIZE * i + j])
            # Якщо це не клітинка, яку необхідно залишити порожньою
            if index != str(EMPTY_SQUARE):
                # Малюємо квадрат по заданним координатам
                c.create_rectangle(
                    j * SQUARE_SIZE,
                    i * SQUARE_SIZE,
                    j * SQUARE_SIZE + SQUARE_SIZE,
                    i * SQUARE_SIZE + SQUARE_SIZE,
                    fill="#43ABC9",
                    outline="#FFFFFF",
                )
                # Пишемо число у центрі квадрата
                c.create_text(
                    j * SQUARE_SIZE + SQUARE_SIZE / 2,
                    i * SQUARE_SIZE + SQUARE_SIZE / 2,
                    text=index,
                    font="Arial {} italic".format(int(SQUARE_SIZE / 4)),
                    fill="#FFFFFF",
                )
