import pgzrun
import random

'''for puzzle'''
laby_color = ['laby_black', 'laby_blue']

# 1表示蓝色, 2表示黑色
laby_self = ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
             (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
             (1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1),
             (1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1),
             (1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1),
             (1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1),
             (1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1),
             (1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1),
             (1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1),
             (1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1),
             (1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1),
             (1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1),
             (1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1),
             (1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1),
             (1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1),
             (1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1),
             (1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1),
             (1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1),
             (1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1),
             (1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1),
             (1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1),
             (1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1),
             (1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1),
             (1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1),
             (1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1),
             (1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1),
             (1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1),
             (1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
             (1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1),
             (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
             (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))

player = Actor('laby_penguin')
player.center = 292.5 - 10 * 24 + 2 * 24, 390 - 15 * 24 + 24
player.success = False
laby_self_loca = {}  # 所有迷宮方格坐标与对应的颜色
laby_self_locajust = []  # 所有迷宮方格坐标
laby_self_loca_black = []  # 黑色方格坐标
laby_self_y = 390 - 15 * 24  # 当前方格的y坐标

# 获得所有迷宮方格的坐标和对应的颜色
for i in laby_self:
    laby_self_x = 292.5 - 10 * 24  # 当前方格的x坐标
    for j in i:
        laby_self_loca[(laby_self_x, laby_self_y)] = laby_color[j]
        laby_self_locajust.append((laby_self_x, laby_self_y))
        if j == 0:
            laby_self_loca_black.append((laby_self_x, laby_self_y))
        laby_self_x += 24
    laby_self_y += 24

# 如果玩家走到了x=292.5, y=702,则是结局2
# 否则是结局1
laby_secondend = 0

laby_past = []  # 记录企鹅现在行走的方向[上, 下, 左, 右]

'''for the movable penguin'''
penguin = Actor('stand')
penguin.pos = 100, 630
penguin.cnt = 0
penguin.toward = 'right'
penguin.appear = False
penguin.comappear = True
penguin.mapapper = False
penguin.goappear = False
penguin.exitappear = False
penguin.chooseappear = False
penguin.startappear = False
penguin.factoryappear = False
penguin.scenememory = 'puzzle'
penguin.puzzlesolved = False
penguin.sudoku = False
'''the Serial number of scene'''
penguin.scene = 'start'
'''Other components'''
component1 = Actor('startbutton')
load = Actor('load')
save = Actor('save')
save.pos = 552, 758
component2 = Actor('nextbutton')
theMap = Actor('map')
bigMap = Actor('bigmap')
gogo = Actor('go')
exitie = Actor('exit')
choose = Actor('choose')
start = Actor('endbutton')
factory = Actor('factory')
success = Actor('puzzle2success')
lazer1 = Actor('puzzlelazer', anchor=('right', 'top'))
lazer1.top = 80
lazer1.left = 500
lazer1.ro = 'left'
lazer2 = Actor('puzzlelazer', anchor=('left', 'top'))
lazer2.top = 130
lazer2.left = 85
lazer2.angle = 80
lazer2.ro = 'left'
head1 = Actor('puzzlelazerhead')
head1.top = 40
head1.right = 530
head2 = Actor('puzzlelazerhead')
head2.top = 90
head2.left = 55

gate = Actor('puzzlegate')
gate.top = 0
gate.left = 260

factory.move = True
factory.stop = False

'''关于谜题2的所有额外设置'''
names = ["adeli", "di", "haibao", "hujing", "nantiaoyan", "xiaolan"]
li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
left = [92.5, 232.5, 372.5, 92.5, 232.5, 372.5, 92.5, 232.5, 372.5, 92.5, 232.5, 372.5, ]
top = [100, 100, 100, 240, 240, 240, 380, 380, 380, 520, 520, 520]
random.shuffle(li)
cnt = 0
things = []
temp1 = Actor('juxing')
temp1.occupied = False
temp1.cnt = 0
for i in li:
    t = Actor('juxing')
    t.cnt = cnt
    t.show = True
    t.name = names[int(i / 2)]
    t.left = left[t.cnt]
    t.top = top[t.cnt]
    things.append(t)
    cnt += 1

'''关于谜题4【数独】的额外设置'''
BOX1 = Rect((67.5, 50), (150, 450))
BOX2 = Rect((150 + 67, 50), (150, 450))
BOX3 = Rect((300 + 67, 50), (150, 450))
BOX4 = Rect((67.5, 50), (450, 150))
BOX5 = Rect((67, 200), (450, 150))
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matrix = [([0] * 9) for i in range(9)]

WIDTH = 585
HEIGHT = 780


def draw():
    screen.clear()
    screen.blit(penguin.scene, (0, 0))
    if penguin.scene == 'start':
        draw1()
    elif penguin.scene == 'telling_stories':
        draw2()
    elif penguin.scene == 'by_accident2':
        draw3()
    elif penguin.scene == 'escape':
        draw4()
    elif penguin.scene == 'puzzle':
        drawpuzzle1()
    elif penguin.scene == 'puzzle1':
        drawpuzzle2()
    elif penguin.scene == 'puzzle3':
        drawpuzzle4()
    elif penguin.scene == 'puzzle2':
        drawpuzzle3()
    elif penguin.scene == 'polluted_factory':
        draw5()
    elif penguin.scene == 'factory0':
        if not penguin.factoryappear:
            draw6()
        else:
            draw7()
    if penguin.appear:  # 每一幕都检查是否出现企鹅
        penguin.draw()
    if penguin.scene != 'start' and penguin.scene != 'the_end':
        # 除了开始和结束页面都需要存档按键
        save.draw()


def update():
    if penguin.scene == 'telling_stories':
        penguin.cnt += 1
        if penguin.cnt > 360:
            penguin.cnt = 0
            penguin.comappear = False
    elif penguin.scene == 'shadow':
        penguin.cnt += 1
        if penguin.cnt > 300:  # 原为 360： 120
            if penguin.scenememory == 'puzzle2':
                penguin.scene = 'polluted_factory'
            else:
                penguin.scene = 'puzzle'
                penguin.appear = True
            penguin.cnt = 0
    elif penguin.scene == 'nakeshadow':
        penguin.cnt += 1
        if penguin.cnt > 300:  # 原为 360： 120
            if penguin.scenememory == 'puzzle':
                penguin.scene = 'puzzle1'
                penguin.appear = True
            elif penguin.scenememory == 'puzzle1':
                penguin.scene = 'puzzle3'
                penguin.appear = False
            elif penguin.scenememory == 'puzzle3':
                penguin.scene = 'puzzle2'
            penguin.cnt = 0
    elif penguin.scene == 'puzzle':
        if lazer1.ro == 'left':
            lazer1.angle -= 0.1
            if lazer1.angle <= -80:
                lazer1.ro = 'right'
        elif lazer1.ro == 'right':
            lazer1.angle += 0.1
            if lazer1.angle >= 60:
                lazer1.ro = 'left'
        if lazer2.ro == 'left':
            lazer2.angle -= 0.2
            if lazer2.angle <= -60:
                lazer2.ro = 'right'
        elif lazer2.ro == 'right':
            lazer2.angle += 0.2
            if lazer2.angle >= 80:
                lazer2.ro = 'left'

        # or lazer2.colliderect(penguin)
        if (lazer1.colliderect(penguin)) and (
                penguin.left >= 0 and penguin.right <= 585):
            print('caught')
            print(penguin.pos)
            print(lazer1.pos)
            print(lazer2.pos)
            penguin.scene = 'captured'
            sounds.cap.play()
            sounds.sad.play()
            sounds.underground.stop()
            penguin.appear = False
        if gate.colliderect(penguin):
            penguin.puzzlesolved = True
    elif penguin.scene == 'polluted_factory':
        penguin.cnt += 1
        if penguin.cnt > 300:
            # 展示三个按键
            penguin.goappear = True
            penguin.exitappear = True
            penguin.chooseappear = True
    elif penguin.scene == 'factory0':
        penguin.cnt += 1
        if penguin.cnt > 180:
            penguin.startappear = True
    if factory.stop and not (penguin.scene == 'the_end'):
        penguin.cnt += 1
        if penguin.cnt > 777:
            penguin.scene = 'the_end'
            penguin.cnt = 0
    if player.success and penguin.scene == 'puzzle2':
        # 当迷宫完成时，如果路线正确
        if laby_secondend:
            penguin.cnt += 1
            if penguin.cnt >= 180:
                penguin.scenememory = 'puzzle2'
                penguin.scene = 'shadow'
                penguin.cnt = 0
        # 如果路线错误
        else:
            penguin.scene = 'captured'
            sounds.sad.play()
            sounds.cap.play()
            sounds.underground.stop()
            penguin.cnt = 0
    if penguin.sudoku and penguin.scene == 'puzzle3':
        penguin.cnt += 1
        if penguin.cnt >= 180:
            penguin.scenememory = 'puzzle3'
            penguin.scene = 'nakeshadow'
            penguin.cnt = 0
    if penguin.scene == 'puzzle2':
        for i in laby_self_loca_black:
            if player.x == i[0] and player.y == i[1]:
                if laby_past[0] == 1:
                    player.y += 24
                elif laby_past[1] == 1:
                    player.y -= 24
                elif laby_past[2] == 1:
                    player.x += 24
                elif laby_past[3] == 1:
                    player.x -= 24


def on_mouse_down(pos):
    global cur_j, cur_i
    if save.collidepoint(pos):  # 存档，不分场景
        sounds.clik.play()
        with open('save_game.txt', 'w') as f:
            f.write(penguin.scene)
            f.write('\n')
            f.write(str(penguin.appear))
            f.write('\n')
            f.write(penguin.scenememory)
    elif penguin.scene == 'start' and load.collidepoint(pos):  # 读档
        sounds.clik.play()
        with open('save_game.txt') as f:
            cnt = 0
            for line in f:
                if cnt == 1:
                    if line == 'False\n':
                        penguin.appear = False
                    else:
                        penguin.appear = True
                elif cnt == 0:
                    penguin.scene = line[:-1]
                elif cnt == 2:
                    penguin.scenememory = line[:-1]
                cnt += 1

    if penguin.scene == 'start' and component1.collidepoint(pos):
        sounds.clik.play()
        penguin.scene = 'telling_stories'
    elif penguin.scene == 'telling_stories' and component2.collidepoint(pos):
        sounds.clik.play()
        penguin.scene = 'by_accident2'
    elif penguin.scene == 'by_accident2' and theMap.collidepoint(pos):
        sounds.map.play()
        penguin.mapapper = True
    elif penguin.scene == 'by_accident2' and component2.collidepoint(pos):
        sounds.clik.play()
        penguin.scene = 'escape'
    elif penguin.scene == 'polluted_factory':
        if gogo.collidepoint(pos):
            sounds.factory.stop()
            sounds.underground.stop()
            sounds.clik.play()
            penguin.scene = 'factory0'
            sounds.new_journey.play()
        elif exitie.collidepoint(pos):
            sounds.factory.stop()
            sounds.clik.play()
            penguin.scene = 'captured'
            sounds.sad.play()
            sounds.cap.play()
            sounds.underground.stop()
        penguin.cnt = 0
    elif penguin.scene == 'factory0':
        if start.collidepoint(pos):
            penguin.factoryappear = True
        if not factory.stop:
            penguin.cnt = 0
    elif penguin.scene == 'puzzle1':
        '''这里可以添加最大尝试次数'''
        for t in things:
            if t.collidepoint(pos):
                sounds.clik.play()
                t.image = t.name  # 翻了过来
                if not temp1.occupied:
                    temp1.occupied = True
                    temp1.cnt = t.cnt
                    temp1.image = t.image
                else:  # 已经掀开了一个
                    if t.image == temp1.image and t.cnt != temp1.cnt:  # 如果匹配成功
                        t.show = False
                        for tt in things:
                            if tt.name == t.image and tt.cnt != t.cnt:
                                tt.show = False
                        print('success')
                    else:  # 如果没有匹配成功
                        print('failed')
                        for tt in things:
                            if tt.image == temp1.image:
                                t.image = 'juxing'
                                tt.image = 'juxing'
                                break
                    temp1.occupied = False
                break
    elif penguin.scene == 'puzzle3':
        cur_j, cur_i = int((pos[0] - 67.5) / 50), int((pos[1] - 50) / 50)


def on_key_down(key):
    if key == key.S:
        penguin.image = 'slip1'
        # set_slip()
    elif key == key.D:
        penguin.image = 'walk1'
    elif key == key.W:
        penguin.image = 'stand'
    elif key == key.A:
        penguin.image = 'backwalk1'
        penguin.toward = 'left'
    elif key == key.SPACE:
        if penguin.image == 'walk1' or penguin.image == 'walk2':
            sounds.walk.play()
            penguin.left += 35  # 原为 15： 75
        elif penguin.image == 'slip1' or penguin.image == 'slip2':
            # 企鹅滑行
            sounds.walk.play()
            penguin.left += 75
        elif penguin.image == 'backwalk1' or penguin.image == 'backwalk2':
            sounds.walk.play()
            penguin.left -= 15

        if penguin.left > WIDTH and penguin.puzzlesolved:
            # 只有满足要求，到达右边界才可以算是场景切换
            penguin.scenememory = penguin.scene
            penguin.scene = 'nakeshadow'
            penguin.appear = False
            penguin.right = 0
        elif penguin.right < 0:
            if penguin.scene == 'puzzle' and not penguin.puzzlesolved:
                pass
            else:
                penguin.left = WIDTH
        set_move()
    elif key == key.E and penguin.scene == 'escape':
        sounds.underground.play(-1)
        penguin.scene = 'shadow'

    global laby_past
    global laby_secondend
    # 向上走
    if key == keys.UP:
        sounds.walk_in_maze.play()
        player.y -= 24
        laby_past = [1, 0, 0, 0]
    # 向下走
    if key == keys.DOWN:
        sounds.walk_in_maze.play()
        player.y += 24
        laby_past = [0, 1, 0, 0]
    # 向左走
    if key == keys.LEFT:
        sounds.walk_in_maze.play()
        player.x -= 24
        laby_past = [0, 0, 1, 0]
    # 向右走
    if key == keys.RIGHT:
        sounds.walk_in_maze.play()
        player.x += 24
        laby_past = [0, 0, 0, 1]
    if player.x == 292.5 and player.y == 702:
        laby_secondend += 1

    global cur_j, cur_i, MATRIX
    if chr(key) in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and (cur_i, cur_j) in BLANK_IJ:
        MATRIX[cur_i][cur_j] = int(chr(key))
        cur_blank_size = sum([1 if col == 0 or col == '0' else 0 for row in MATRIX for col in row])


def set_move():
    if penguin.image == 'slip1' or penguin.image == 'slip1':
        set_slip()
    elif penguin.image == 'walk1' or penguin.image == 'walk2':
        set_walk()
    else:
        set_backwalk()


def set_slip():
    penguin.image = 'slip2'
    clock.schedule_unique(set_slip_normal, 0.5)


def set_slip_normal():
    if penguin.image == 'slip2':
        penguin.image = 'slip1'


def set_walk():
    penguin.image = 'walk2'
    clock.schedule_unique(set_walk_normal, 0.5)


def set_walk_normal():
    if penguin.image == 'walk2':
        penguin.image = 'walk1'
    else:
        penguin.image = 'walk2'


def set_backwalk():
    penguin.image = 'backwalk2'
    clock.schedule_unique(set_backwalk_normal, 0.5)


def set_backwalk_normal():
    if penguin.image == 'backwalk2':
        penguin.image = 'backwalk1'
    else:
        penguin.image = 'backwalk2'


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
            __matrix = build_game(_matrix, next_i, next_j, _number)
            if __matrix and sum([sum(row) for row in __matrix]) == (sum(range(1, 10)) * 9):
                return __matrix
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


def draw1():
    component1.pos = 292, 620
    load.pos = 292, 700
    component1.draw()
    load.draw()


def draw2():
    if penguin.comappear:
        s = 'stories'
        if int(penguin.cnt / 30 - 4) < 0:
            return
        s += str(int(penguin.cnt / 30 - 4))
        # draw2()
        component = Actor(s)
        component.pos = 292, 220
        component.draw()
    else:
        component = Actor('stories8')
        component.pos = 292, 220
        component.draw()
        component2.pos = 292, 370
        component2.draw()


def draw3():
    theMap.pos = 400, 700
    theMap.draw()
    if penguin.mapapper:
        bigMap.pos = 292, 200
        bigMap.draw()
        component2.pos = 400, 350
        component2.draw()


def draw4():
    screen.draw.text('  Clue: will you ESCAPE?  ', (20, 750), color='black', background='LightSkyBlue1')


def draw5():
    sounds.factory.play()
    if penguin.chooseappear:
        choose.pos = 292, 200
        gogo.pos = 212, 290
        exitie.pos = 372, 290
        choose.draw()
        gogo.draw()
        exitie.draw()


def draw6():
    if penguin.startappear:
        start.pos = 292, 700
        start.draw()


def draw7():
    if penguin.factoryappear:
        if factory.move:
            factory.bottom = 780
            factory.draw()
            screen.clear()
            factory.move = False
            print('let\'s move!')  # 控制台检查能否正常运行
        if not factory.stop:
            # 工厂图片滚动效应
            factory.top += 1
        factory.draw()
        if factory.top >= 0:
            factory.stop = True


def drawpuzzle1():
    lazer1.draw()
    lazer2.draw()
    gate.draw()
    head1.draw()
    head2.draw()


def drawpuzzle2():
    for t in things:
        if t.show:
            t.draw()


def drawpuzzle4():
    screen.draw.rect(BOX1, (0, 0, 0))
    screen.draw.rect(BOX2, (0, 0, 0))
    screen.draw.rect(BOX3, (0, 0, 0))
    screen.draw.rect(BOX4, (0, 0, 0))
    screen.draw.rect(BOX5, (0, 0, 0))
    # 用户点中格子变成蓝色
    BOX = Rect((cur_j * 50 + 2.5 + 67.5, cur_i * 50 + 2.5 + 50, 50 - 5, 50 - 5))
    screen.draw.filled_rect(BOX, 'blue')

    # 绘制九宫格中的数字，包括本来就有的，以及用户填入的，本来就在的用灰色，用户填入的如何合法则为绿色，否则为红色，是一种提示
    for i in range(len(MATRIX)):
        for j in range(len(MATRIX[0])):
            _color = check_color(MATRIX, i, j) if (i, j) in BLANK_IJ else ('gray')
            x, y = j * 50 + 15 + 67.5, i * 50 + 15 + 50
            screen.draw.text(str(MATRIX[i][j] if MATRIX[i][j] not in [0, '0'] else ''), (x, y), fontsize=50,
                             color=_color)
    if check_win(MATRIX_ANSWER, MATRIX):
        # screen.draw.text("success", (100, 200), fontsize=100, color='pink')
        penguin.sudoku = True
        success.pos = 292, 350
        success.draw()


def drawpuzzle3():
    for i in laby_self_locajust:
        t = Actor(laby_self_loca[i])
        t.center = i[0], i[1]
        t.draw()
    # 画企鹅
    player.draw()

    # 如果抵达终点, 则显示success
    if player.x == 100.5 and player.y == 726:
        # screen.draw.text("success", (280, 390))
        success.pos = 292, 350
        success.draw()
        player.success = True

    if laby_secondend > 0:
        # 显示结局2
        pass
    else:
        # 显示结局1
        pass


# check win or not
global cur_j, cur_i, MATRIX
cur_i, cur_j = 0, 0
cur_blank_size = 1  # 修改这里可以控制数独的难度，数字越大，难度越大
MATRIX_ANSWER, MATRIX, BLANK_IJ = give_me_a_game(blank_size=cur_blank_size)
print_matrix(MATRIX)
print_matrix(MATRIX_ANSWER)

pgzrun.go()
