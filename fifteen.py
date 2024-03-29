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


def click(event):
    # Отримуємо координати кліка
    x, y = event.x, event.y
    # Конвертуємо координати з пікселів у клітини
    x = x // SQUARE_SIZE
    y = y // SQUARE_SIZE
    # Отримуємо індекс у списку об'єкта за яким ми натиснули
    board_index = x + (y * BOARD_SIZE)
    # Отримуємо індекс порожньої клітки у списку.
    empty_index = get_empty_neighbor(board_index)
    # Змінюємо місцями порожню клітку і клітку, якою клікнули
    board[board_index], board[empty_index] = board[empty_index], board[board_index]
    # Перемальовуємо ігрове поле
    draw_board()
    # Якщо поточний стан дошки відповідає правильному – малюємо повідомлення про перемогу
    if board == correct_board:
        show_victory_plate()


c.bind("<Button-1>", click)


def get_empty_neighbor(index):
    # Отримуємо індекс порожньої клітини у списку
    empty_index = board.index(EMPTY_SQUARE)
    # Дізнаємося відстань від порожньої клітини до клітини якою клікнули
    abs_value = abs(empty_index - index)
    # Якщо порожня клітина над або під клітиною на яку клікнули
    # Повертаємо індекс порожньої клітини
    if abs_value == BOARD_SIZE:
        return empty_index
    # Якщо порожня клітина ліворуч чи праворуч
    elif abs_value == 1:
        # Перевіряємо, щоб блоки були в одному ряді
        max_index = max(index, empty_index)
        if max_index % BOARD_SIZE != 0:
            return empty_index
    # Поруч із блоком не було порожнього поля
    return index


def is_solvable():
    """Функція визначає, чи має головоломка рішення"""
    num_inversions = get_inv_count()
    if BOARD_SIZE % 2 != 0:
        return num_inversions % 2 == 0
    else:
        empty_square_row = BOARD_SIZE - (board.index(EMPTY_SQUARE) // BOARD_SIZE)
        if empty_square_row % 2 == 0:
            return num_inversions % 2 != 0
        else:
            return num_inversions % 2 == 0


def show_victory_plate():
    # Малюємо чорний квадрат по центру поля
    c.create_rectangle(
        SQUARE_SIZE / 5,
        SQUARE_SIZE * BOARD_SIZE / 2 - 10 * BOARD_SIZE,
        BOARD_SIZE * SQUARE_SIZE - SQUARE_SIZE / 5,
        SQUARE_SIZE * BOARD_SIZE / 2 + 10 * BOARD_SIZE,
        fill="#000000",
        outline="#FFFFFF",
    )
    # Пишемо червоним текст "Перемога"
    c.create_text(
        SQUARE_SIZE * BOARD_SIZE / 2,
        SQUARE_SIZE * BOARD_SIZE / 1.9,
        text="ПОБЕДА!",
        font="Helvetica {} bold".format(int(10 * BOARD_SIZE)),
        fill="#DC143C",
    )


def get_inv_count():
    """Функція, яка повертає кількість переміщень"""
    inversions = 0
    inversion_board = board[:]
    inversion_board.remove(EMPTY_SQUARE)
    for i in range(len(inversion_board)):
        first_item = inversion_board[i]
        for j in range(i + 1, len(inversion_board)):
            second_item = inversion_board[j]
            if first_item > second_item:
                inversions += 1
    return inversions


# Список з яким ми порівнюватимемо результат. В даному випадку це
# просто відсортований список, але при бажанні можна придумати щось інше
correct_board = board[:]
# перемішуємо блоки
shuffle(board)
while not is_solvable():
    shuffle(board)
# Малюємо дошку
draw_board()
root.mainloop()
