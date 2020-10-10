import pgzrun

penguin = Actor('stand')
penguin.pos = 100, 150
penguin.cnt = 0

WIDTH = 700
HEIGHT = penguin.height + 50


def draw():
    screen.clear()
    screen.fill((128, 0, 0))
    penguin.draw()


def update():
    penguin.cnt += 1
    if penguin.cnt == 30 and penguin.image == 'walk1':
        set_walk()
    elif penguin.cnt == 30 and penguin.image == 'slip1':
        set_slip()
    elif penguin.cnt == 60:
        penguin.cnt = 0
    penguin.left += 1
    if penguin.left > WIDTH:
        penguin.left = 0


def set_walk():
    penguin.image = 'walk2'
    clock.schedule_unique(set_walk_normal, 0.5)


def set_walk_normal():
    if penguin.image == 'walk2':
        penguin.image = 'walk1'


def on_key_down(key):
    if key == key.S:
        penguin.image = 'slip1'
        set_slip()


def set_slip():
    penguin.image = 'slip2'
    clock.schedule_unique(set_slip_normal, 0.5)


def set_slip_normal():
    if penguin.image == 'slip2':
        penguin.image = 'slip1'


pgzrun.go()
