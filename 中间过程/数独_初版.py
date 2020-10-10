import pgzrun
from build import print_matrix,give_me_a_game,check
import sys

#绘制背景
WIDTH = 900
HEIGHT = 900
BOX1 = Rect((0,0),(300,900))
BOX2 = Rect((300,0),(300,900))
BOX3 = Rect((0,0),(900,300))
BOX4 = Rect((0,300),(900,300))
BOX5 = Rect((0,600),(900,300))
def draw():
    screen.fill((255,255,255))
    screen.draw.rect(BOX1,(0,0,0))
    screen.draw.rect(BOX2,(0,0,0))
    screen.draw.rect(BOX3,(0,0,0))
    screen.draw.rect(BOX4,(0,0,0))
    screen.draw.rect(BOX5,(0,0,0))

#用户点中格子变成蓝色
def draw_choose():
  BOX = Rect((cur_j*100+5,cur_i*100+5,100-10,100-10))
  screen.draw.rect(BOX,'blue')

#绘制九宫格中的数字，包括本来就有的，以及用户填入的，本来就在的用灰色，用户填入的如何合法则为绿色，否则为红色，是一种提示
def draw_number():
  for i in range(len(MATRIX)):
    for j in range(len(MATRIX[0])):
      _color = check_color(MATRIX,i,j) if (i,j) in BLANK_IJ else COLORS['gray']
      txt = font80.render(str(MATRIX[i][j] if MATRIX[i][j] not in [0,'0'] else ''),True,_color)
      x,y = j*100+30,i*100+10
      screen.blit(txt,(x,y))

def on_mouse_down(pos):
    cur_j,cur_i = int(pos[0]/100),int(pos[1]/100)
def  on_key_down(key):
    if chr(key) in ['1','2','3','4','5','6','7','8','9'] and (cur_i,cur_j) in BLANK_IJ:
                MATRIX[cur_i][cur_j] = int(chr(event.key))
                cur_blank_size = sum([1 if col==0 or col=='0' else 0 for row in MATRIX for col in row])
                cur_change_size +=1
def check_win(matrix_all,matrix):
    if matrix_all == matrix:
        return True
    return False
def check_color(matrix,i,j):
    _matrix = [[col for col in row]for row in matrix]
    _matrix[i][j] = 0
    if check(_matrix,i,j,matrix[i][j]):
        return ('green')
    return ('red')
def draw_number():
    for i in range(len(MATRIX)):
        for j in range(len(MATRIX[0])):
            _color = check_color(MATRIX,i,j) if (i,j) in BLANK_IJ else COLORS['gray']
            txt = font80.render(str(MATRIX[i][j] if MATRIX[i][j] not in [0,'0'] else ''),True,_color)
            x,y = j*100+30,i*100+10
            screen.blit(txt,(x,y))
def draw_context():
    txt = font100.render('Blank:'+str(cur_blank_size)+'   Change:'+str(cur_change_size),True,(0,0,0))
    x,y = 10,900
    screen.blit(txt,(x,y))
    running = True
    while running:
        # choose item
        draw_choose()
        # numbers
        draw_number()
        #check win or not
        if check_win(MATRIX_ANSWER,MATRIX):
            print('You win, smarty ass!!!')
            break

pgzrun.go()