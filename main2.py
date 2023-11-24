# Итак, мы имеем:
#
# Игру «Крестики-нолики».
# Консоль, куда будет выводиться ход игры. Тут делать красиво мы умеем с помощью форматированных строк.
# Неутолимое желание написать что-то реальное своими руками.
# Размер поля предполагается равным 3x3.
#
# Пример печати поля в консоль:
#    0 1 2
# 0  X X 0
# 1  0 X 0
# 2  - 0 -
#

def print_play_field(field):
    print('   0 1 2')
    for i in range(3):
        print(f'{i} ', *field[i])


def get_coordinates(field, element_is_cross):
    while True:
        coordinates = input(
            'Введите координаты хода ' + ('крестиком' if element_is_cross else 'ноликом') +
            ' в формате \'X Y\', где X-столбец, а Y-строка (q - выход): ').split()
        if coordinates[0] == 'q':
            exit(0)
        if len(coordinates) != 2:
            print('Формат ввода не соответствует запрашиваемому \'X Y\'!')
        elif not (coordinates[0].isnumeric() and coordinates[1].isnumeric()):
            print('Необходимо вводить только положительные целые числа!')
        elif not (int(coordinates[0]) in range(3) and int(coordinates[1]) in range(3)):
            print('Необходимо вводить числа в диапазоне от 0 до 2!')
        elif field[int(coordinates[1])][int(coordinates[0])] != '-':
            print('Ячейка занята. Выберите другую!')
        else:
            return int(coordinates[1]), int(coordinates[0])


def win_combination(field):
    # Проверяем по вертикали и горзонтали
    for i in range(3):
        if field[i][i] != '-' and (
                field[0][i] == field[1][i] == field[2][i] or field[i][0] == field[i][1] == field[i][2]):
            return True
    # Проверяем обе диагонали
    if field[1][1] != '-' and (
            field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0]):
        return True
    return False


def main():
    play_field = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]  # Игровое поле
    current_is_cross = True  # Начинаем игру всегда с крестика
    play_count = None  # Счетчик ходов
    for play_count in reversed(range(9)):
        print_play_field(play_field)
        x, y = get_coordinates(play_field, current_is_cross)
        play_field[x][y] = 'X' if current_is_cross else '0'
        if win_combination(play_field):
            break
        current_is_cross = not current_is_cross  # Меняем текущий тип элемента (крестик или нет)
    print_play_field(play_field)
    if play_count:
        print('Выиграли', 'крестики!' if current_is_cross else 'нолики!')
    else:
        print('Ничья!')