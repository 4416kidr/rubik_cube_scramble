def flex(cube, r, ind):
    for i in range(ind):
        cube = rotate_cube(cube, r)
    return cube

def rotate_cube(cube, r):
    """ info: rotate cube for all
        arg: cube, side, ind, rside
        return: changed cube
    """

    """ アルゴリズム
        #違う面に移動する処理

        R回転
        G258, W258, B630, Y258
        rcolor = list('GWBY')
        rblock = [[2, 5, 8], [2, 5, 8], [6, 3, 0], [2, 5, 8]]
        rside = 3
        各回転の移動先は関数によって取得する

        kari = Y(3, 5)
        Y(3, 5) = B(2, 4)
        B(2, 4) = W(1, 0)
        W(1, 0) = G(0, 2)
        G(0, 2) = kari = Y(3, 5)

        #同じ面で回転する処理
        |012|  -->  |630|
        |345|  -->  |741|
        |678|  -->  |852|
        [6, 3, 0, 7, 4, 1, 8, 5, 2]
    """

    sc, sb, rside = get_list(r)
    # rcolor = list('GRBO')
    # rblock = [[6, 7, 8], [6, 7, 8], [6, 7, 8], [6, 7, 8]]

    # set first to kari
    kc = int(sc[3]) # 1(O)
    kb = tuple(sb[3]) # [6, 7, 8]
    
    kari = list()
    for i in range(len(kb)):
        kari.append(cube[kc][kb[i]])

    # swap
    for i in range(len(sc)-1): #4面中3面移動する
        for j in range(len(sb[0])): #3ブロック移動する
            cube[sc[3-i]][sb[3-i][j]] = str(cube[sc[2-i]][sb[2-i][j]])
    
    # set last from kari
    for i in range(len(kb)):
        cube[sc[0]][sb[0][i]] = str(kari[i])
    
    # rotate side
    cube[rside] = rotate_side(cube[rside])
    return cube

def rotate_side(side):
    new = list()
    rlist = [6, 3, 0, 7, 4, 1, 8, 5, 2]
    for i in range(len(side)):
        new.append(side[rlist[i]])
    
    return new

def get_list(r):
    rcolor = list()
    rblock = list()
    rside = -1
    if r == 'B':
        # GOBR-0000-1111-2222
        rcolor = list('GOBR')
        rblock = [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
        rside = 0
    elif r == 'L':
        # GYBW-0080-3353-6626
        rcolor = list('GYBW')
        rblock = [[0, 3, 6], [0, 3, 6], [8, 5, 2], [0, 3, 6]]
        rside = 1
    elif r == 'U':
        # WRYO-6028-7315-8602
        rcolor = list('WRYO')
        rblock = [[6, 7, 8], [0, 3, 6], [2, 1, 0], [8, 5, 2]]
        rside = 2
    elif r == 'R':
        # GWBY-2262-5535-8808
        rcolor = list('GWBY')
        rblock = [[2, 5, 8], [2, 5, 8], [6, 3, 0], [2, 5, 8]]
        rside = 3
    elif r == 'D':
        # WOYR-0682-1375-2068

        rcolor = list('WOYR')
        rblock = [[0, 1, 2], [6, 3, 0], [8, 7, 6], [2, 5, 8]]
        rside = 4
    elif r == 'F':
        # GRBO-6666-7777-8888
        rcolor = list('GRBO')
        rblock = [[6, 7, 8], [6, 7, 8], [6, 7, 8], [6, 7, 8]]
        rside = 5
    
    #文字を数値へと変換する
    cstr = list('WOGRBY')
    for i in range(len(rcolor)):
        ind = cstr.index(rcolor[i])
        rcolor[i] = ind
    return rcolor, rblock, rside

""" UFRDBL
    # U
    # before = [W6, W7, W8, R0, R3, R6, Y2, Y1, Y0, O8, O5, O2]
    # WRYO-6028-7315-8602
    # before = [[W, [6, 7, 8]], [R, [0, 3, 6]], [Y, [2, 1, 0]], [O, [8, 5, 2]]]

    # F
    # before = [G6, G7, G8, R6, R7, R8, B6, B7, B8, O6, O7, O8]
    # GRBO-6666-7777-8888
    # before = [[G, [6, 7, 8]], [R, [6, 7, 8]], [B, [6, 7, 8]], [O, [6, 7, 8]]]

    # R
    # before = [G2, G5, G8, W2, W5, W8, B6, B3, B0, Y2, Y5, Y8]
    # GWBY-2262-5535-8808
    # before = [[G, [2, 5, 8]], [W, [2, 5, 8]], [B, [6, 3, 0]], [Y, [2, 5, 8]]]

    # D
    # before = [Y6, Y7, Y8, R8, R5, R2, W2, W1, W0, O0, O3, O6]
    # WOYR-0682-1375-2068
    # before = [[W, [0, 1, 2]], [O, [6, 3, 0]], [Y, [8, 7, 6]], [R, [2, 5, 8]]]

    # B
    # before = [G0, G1, G2, O0, O1, O2, B0, B1, B2, R0, R1, R2]
    # GOBR-0000-1111-2222
    # before = [[G, [0, 1, 2]], [O, [0, 1, 2]], [B, [0, 1, 2]], [R, [0, 1, 2]]]

    # L
    # before = [G0, G3, G6, Y0, Y3, Y6, B8, B5, B2, W0, W3, W6]
    # GYBW-0080-3353-6626
    # before = [[G, [0, 3, 6]], [Y, [0, 3, 6]], [B, [8, 5, 2]], [W, [0, 3, 6]]]
"""
