import pgzrun

penguin = Actor('stand')
penguin.pos = 100, 630
penguin.cnt = 0
penguin.toward = 'right'
scene = 'start'

WIDTH = 585
# HEIGHT = penguin.height + 50
HEIGHT = 780


def draw():
    screen.clear()
    # screen.fill((128, 0, 0))
    screen.blit("start", (0, 0))
    penguin.draw()


def update():
    penguin.cnt += 1
    # if penguin.cnt == 30 and penguin.image == 'walk1':
    #     set_walk()
    # elif penguin.cnt == 30 and penguin.image == 'slip1':
    #     set_slip()
    if penguin.cnt == 60:
        penguin.cnt = 0
    # penguin.left += 1
    # if penguin.left > WIDTH:
    #    penguin.left = 0


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
            penguin.left += 15
        elif penguin.image == 'slip1' or penguin.image == 'slip2':
            penguin.left += 35
        elif penguin.image == 'backwalk1' or penguin.image == 'backwalk2':
            penguin.left -= 15

        if penguin.left > WIDTH:
            penguin.right = 0
        elif penguin.right < 0:
            penguin.left = WIDTH
        set_move()


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


pgzrun.go()
