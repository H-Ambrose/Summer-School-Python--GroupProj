import pgzrun


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
penguin.puzzlecnt = 0
'''the Serial number of scene'''
penguin.scene = 'start'
'''Other components'''
component1 = Actor('startbutton')
component2 = Actor('nextbutton')
theMap = Actor('map')
bigMap = Actor('bigmap')
gogo = Actor('go')
exitie = Actor('exit')
choose = Actor('choose')
start = Actor('endbutton')
factory = Actor('factory')
factory.move = True
factory.stop = False

WIDTH = 585
# HEIGHT = penguin.height + 50
HEIGHT = 780


def draw():
    screen.clear()
    # screen.fill((128, 0, 0))
    screen.blit(penguin.scene, (0, 0))
    if penguin.scene == 'start':
        draw1()
    elif penguin.scene == 'telling_stories':
        draw2()
    elif penguin.scene == 'by_accident2':
        draw3()
    elif penguin.scene == 'escape':
        draw4()
    elif penguin.scene == 'polluted_factory':
        draw5()
    elif penguin.scene == 'factory0':
        if not penguin.factoryappear:
            draw6()
        else:
            draw7()
    if penguin.appear:
        penguin.draw()


def update():
    if penguin.scene == 'telling_stories':
        penguin.cnt += 1
        if penguin.cnt > 360:
            penguin.cnt = 0
            penguin.comappear = False
    elif penguin.scene == 'shadow' or penguin.scene == 'nakeshadow':
        penguin.cnt += 1
        if penguin.cnt > 60:  # 原为 360
            if penguin.puzzlecnt < 3:
                penguin.scene = 'puzzle'
                penguin.appear = True
                print('already enter puzzle')
            else:
                penguin.scene = 'polluted_factory'
                penguin.appear = False
            penguin.cnt = 0
    elif penguin.scene == 'polluted_factory':
        penguin.cnt += 1
        if penguin.cnt > 300:
            penguin.goappear = True
            penguin.exitappear = True
            penguin.chooseappear = True
    elif penguin.scene == 'factory0':
        penguin.cnt += 1
        if penguin.cnt > 180:
            penguin.startappear = True
    elif penguin.scene == 'puzzle':
        penguin.cnt += 1
        if penguin.cnt >= 60:
            penguin.cnt = 0
    # penguin.left += 1
    # if penguin.left > WIDTH:
    #    penguin.left = 0
    if factory.stop and not(penguin.scene == 'the_end'):
        penguin.cnt += 1
        print(penguin.cnt)
        if penguin.cnt > 1300:
            penguin.scene = 'the_end'
            penguin.cnt = 0


def on_mouse_down(pos):
    if penguin.scene == 'start' and component1.collidepoint(pos):
        penguin.scene = 'telling_stories'
    elif penguin.scene == 'telling_stories' and component2.collidepoint(pos):
        penguin.scene = 'by_accident2'
    elif penguin.scene == 'by_accident2' and theMap.collidepoint(pos):
        penguin.mapapper = True
    elif penguin.scene == 'by_accident2' and component2.collidepoint(pos):
        penguin.scene = 'escape'
    elif penguin.scene == 'polluted_factory':
        if gogo.collidepoint(pos):
            penguin.scene = 'factory0'
        elif exitie.collidepoint(pos):
            penguin.scene = 'captured'
        penguin.cnt = 0
    elif penguin.scene == 'factory0':
        if start.collidepoint(pos):
            penguin.factoryappear = True
        if not factory.stop:
            penguin.cnt = 0


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
            penguin.left += 75  # 原为 15
        elif penguin.image == 'slip1' or penguin.image == 'slip2':
            penguin.left += 35
        elif penguin.image == 'backwalk1' or penguin.image == 'backwalk2':
            penguin.left -= 15

        if penguin.left > WIDTH:
            if penguin.scene == 'puzzle':
                penguin.scene = 'nakeshadow'
                penguin.puzzlecnt += 1
                penguin.appear = False
            penguin.right = 0
        elif penguin.right < 0:
            penguin.left = WIDTH
        set_move()
    elif key == key.E and penguin.scene == 'escape':
        penguin.scene = 'shadow'


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


def draw1():
    component1.pos = 292, 620
    component1.draw()


def draw2():
    if penguin.comappear:
        s = 'stories'
        if int(penguin.cnt / 30 - 4) < 0:
            return
        s += str(int(penguin.cnt / 30 - 4))
        # draw2()
        component = Actor(s)
        # print(s)
        component.pos = 292, 220
        component.draw()
    else:
        component = Actor('stories8')
        # print(s)
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
            print('let\'s move!')
        if not factory.stop:
            factory.top += 0.5
        factory.draw()
        # print(factory.top)
        if factory.top >= 0:
            factory.stop = True


pgzrun.go()
