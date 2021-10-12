import definition as defin
dcolor = defin.color()

class Rotate_data:
    color, block, side = (), (), -1
    def __init__(self, c, b, s):
        self.color = c
        self.block = b
        self.side = s
    def get(self):
        return self.color, self.block, self.side

rotate_data = []

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

    rl = tuple('ULFRBD')
    rotate = rotate_data[rl.index(r)]
    sc, sb, rside = rotate.get()

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


def initialize():

    global rotate_data
    rd = Rotate_data

    # ULFRBD
    db = (
        (['G012', 'O012', 'B012', 'R012'], 'W'), # U
        (['W036', 'G036', 'Y036', 'B852'], 'O'), # L
        (['W678', 'R036', 'Y210', 'O852'], 'G'), # F
        (['G258', 'W258', 'B630', 'Y258'], 'R'), # R
        (['W012', 'O630', 'Y876', 'R258'], 'B'), # B
        (['G678', 'R678', 'B678', 'O678'], 'Y'), # D
        )

    for i in range(len(db)):
        a, b, c = transform(db[i][0], db[i][1])
        rd = Rotate_data(a, b, c)
        rotate_data.append(rd)

def transform(rl, side):
    # GOBR -> [2, 1, 4, 3]
    color_list = [color_to_number(l[0]) for l in rl]
    
    side = color_to_number(side)
    # ['258', '258', '630', '258']
    block_list = [l[1: ] for l in rl]
    # [[2, 5, 8], [2, 5, 8], [6, 3, 0], [2, 5, 8]]
    block_list = [list(map(int, l)) for l in block_list]

    return color_list, block_list, side

def color_to_number(color):
    """ 
    文字を数値へと変換する
    """
    if color in dcolor:
        ind = dcolor.index(color)
        return ind

initialize()