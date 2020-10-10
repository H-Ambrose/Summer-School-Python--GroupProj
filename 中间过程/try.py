import random
import pgzrun
import numpy as np

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

WIDTH = 585
# HEIGHT = penguin.height + 50
HEIGHT = 780


def draw():
    screen.clear()
    drawpuzzle2()


def on_mouse_down(pos):
    for t in things:
        if t.collidepoint(pos):
            t.image = t.name  # 翻了过来
            if not temp1.occupied:
                temp1.occupied = True
                temp1.cnt = t.cnt
                temp1.image = t.image
            else:  # 已经掀开了一个
                if t.image == temp1.image:  # 如果匹配成功
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


# def set_block(a1, a2):
#     clock.schedule_unique(set_back, 1.0)


def drawpuzzle2():
    print('ENTER')
    for t in things:
        print(t.show, end=' ')
        if t.show:
            t.draw()


pgzrun.go()
