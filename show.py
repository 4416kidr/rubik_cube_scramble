"""

=================
|   |www|   |   |
|   |www|   |   |
|   |www|   |   |
=================
|ooo|ggg|rrr|bbb|
|ooo|ggg|rrr|bbb|
|ooo|ggg|rrr|bbb|
=================
|   |yyy|   |   |
|   |yyy|   |   |
|   |yyy|   |   |
=================

展開図形式へcubeを変更
二重線で区切る
1. 3*3の面を完成させる
2. 面を4つ集めて、結合させる
3. 二重線で区切る
1-3を3回繰り返す
二重線で区切る

"""

length = 6*4 + 5
wbar = "="*length
space = ' '*6
vvar = '|'

def show_cube(cube):
    """
    arg: cube
    info: show cube state by text
    """

    line = []
    for i in range(3*3+4):
        if i % 4 == 0:
            line.append(wbar)
        else:
            line.append('')

    tline = [[], [], []]    
    tline[0] = make_3line(cube, [-1, 0, -1, -1])
    tline[1] = make_3line(cube, [1, 2, 3, 4])
    tline[2] = make_3line(cube, [-1, 5, -1, -1])


    for i in range(3):
        for j in range(len(tline[i])):
            line[4*i + j + 1] = tline[i][j]
    
    for i in range(len(line)):
        print(line[i])


def make_3line(cube, side_list):
    line = [vvar, vvar, vvar]
    side_result = []
    for i in side_list:
        if i == -1:
            for j in range(3):
                line[j] += space + vvar
            continue
        side_result = make_side(cube[i])
        for j in range(3):
            line[j] += side_result[j] + vvar
    return line



def make_side(side):
    li = ['', '', '']
    for i in range(len(side)):
        if int(i/3) == 0:
            li[0] += str(side[i])
        elif int(i/3) == 1:
            li[1] += str(side[i])
        elif int(i/3) == 2:
            li[2] += str(side[i])
    return li



    


