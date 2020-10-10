import pgzrun
from build import print_matrix, give_me_a_game, check
import random

# 绘制背景
WIDTH = 585
HEIGHT = 780
BOX1 = Rect((0, 0), (150, 450))
BOX2 = Rect((150, 0), (150, 450))
BOX3 = Rect((0, 0), (450, 150))
BOX4 = Rect((0, 150), (450, 150))
BOX5 = Rect((0, 300), (450, 150))


def draw():
    global cur_j, cur_i
    screen.fill((255, 255, 255))
    screen.draw.rect(BOX1, (0, 0, 0))
    screen.draw.rect(BOX2, (0, 0, 0))
    screen.draw.rect(BOX3, (0, 0, 0))
    screen.draw.rect(BOX4, (0, 0, 0))
    screen.draw.rect(BOX5, (0, 0, 0))
    # 用户点中格子变成蓝色
    BOX = Rect((cur_j * 50 + 2.5, cur_i * 50 + 2.5, 50 - 5, 50 - 5))
    screen.draw.filled_rect(BOX, 'blue')

    # 绘制九宫格中的数字，包括本来就有的，以及用户填入的，本来就在的用灰色，用户填入的如何合法则为绿色，否则为红色，是一种提示
    for i in range(len(MATRIX)):
        for j in range(len(MATRIX[0])):
            _color = check_color(MATRIX, i, j) if (i, j) in BLANK_IJ else ('gray')
            x, y = j * 50 + 15, i * 50 + 15
            screen.draw.text(str(MATRIX[i][j] if MATRIX[i][j] not in [0, '0'] else ''), (x, y), fontsize=50,
                             color=_color)


# 生成数独
def print_matrix(matrix):
    print('—' * 19)
    for row in matrix:
        print('|' + ' '.join([str(col) for col in row]) + '|')
    print('—' * 19)


def shuffle_number(_list):
    random.shuffle(_list)
    return _list


def check(matrix, i, j, number):
    if number in matrix[i]:
        return False
    if number in [row[j] for row in matrix]:
        return False
    group_i, group_j = int(i / 3), int(j / 3)
    if number in [matrix[i][j] for i in range(group_i * 3, (group_i + 1) * 3) for j in
                  range(group_j * 3, (group_j + 1) * 3)]:
        return False
    return True


def build_game(matrix, i, j, number):
    if i > 8 or j > 8:
        return matrix
    if check(matrix, i, j, number):
        _matrix = [[col for col in row] for row in matrix]
        _matrix[i][j] = number
        next_i, next_j = (i + 1, 0) if j == 8 else (i, j + 1)
        for _number in shuffle_number(number_list):
            # _matrixs.append(build_game(_matrix,next_i,next_j,_number))
            __matrix = build_game(_matrix, next_i, next_j, _number)
            if __matrix and sum([sum(row) for row in __matrix]) == (sum(range(1, 10)) * 9):
                return __matrix
    # return _matrixs
    return None


def give_me_a_game(blank_size=9):
    matrix_all = build_game(matrix, 0, 0, random.choice(number_list))
    set_ij = set()
    while len(list(set_ij)) < blank_size:
        set_ij.add(
            str(random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])) + ',' + str(random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])))
    matrix_blank = [[col for col in row] for row in matrix_all]
    blank_ij = []
    for ij in list(set_ij):
        i, j = int(ij.split(',')[0]), int(ij.split(',')[1])
        blank_ij.append((i, j))
        matrix_blank[i][j] = 0
    return matrix_all, matrix_blank, blank_ij


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matrix = [([0] * 9) for i in range(9)]
if __name__ == "__main__":
    print_matrix(build_game(matrix, 0, 0, random.choice(number_list)))


def on_mouse_down(pos):
    global cur_j, cur_i
    cur_j, cur_i = int(pos[0] / 50), int(pos[1] / 50)


def on_key_down(key):
    global cur_j, cur_i
    if chr(key) in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and (cur_i, cur_j) in BLANK_IJ:
        MATRIX[cur_i][cur_j] = int(chr(key))
        cur_blank_size = sum([1 if col == 0 or col == '0' else 0 for row in MATRIX for col in row])


def check_win(matrix_all, matrix):
    if matrix_all == matrix:
        return True
    return False


def check_color(matrix, i, j):
    _matrix = [[col for col in row] for row in matrix]
    _matrix[i][j] = 0
    if check(_matrix, i, j, matrix[i][j]):
        return ('green')
    return ('red')
    # choose item
    draw_choose()
    # numbers
    draw_number()


# check win or not
global cur_j, cur_i
cur_i, cur_j = 0, 0
cur_blank_size = 50
MATRIX_ANSWER, MATRIX, BLANK_IJ = give_me_a_game(blank_size=cur_blank_size)
print_matrix(MATRIX)
if check_win(MATRIX_ANSWER, MATRIX):
    screen.draw.text('success')
print_matrix(MATRIX_ANSWER)
pgzrun.go()
