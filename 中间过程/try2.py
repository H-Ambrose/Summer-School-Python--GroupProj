with open('save_game.txt') as f:
    for line in f:
        if line == '0':
            print(False)
        else:
            print(line)

with open('save_game.txt', 'w') as f:
    f.write('I love programming!\nand you')
