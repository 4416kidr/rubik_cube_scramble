def R(cube):
    """
    arg: cube
    return: changed cube

    info: rotate cube as R
    side = [2, 5, 4, 0] # 0 -> 4 -> 5 -> 2
    ind = [2, 5, 8]
    rside = 3
    """
    side = [2, 5, 4, 0] # 0 -> 4 -> 5 -> 2
    ind = [2, 5, 8]
    rside = 3
    cube = rotate_cube(cube, side, ind, rside)

    return cube

def F(cube):
    """
    arg: cube
    return: changed cube
    
    info: rotate cube as F
    side = [4, 3, 2, 1] # 1 -> 2 -> 3 -> 4
    ind = [6, 7, 8]
    rside = 5
    """
    side = [4, 3, 2, 1] # 1 -> 2 -> 3 -> 4
    ind = [6, 7, 8]
    rside = 5
    cube = rotate_cube(cube, side, ind, rside)

    return cube

def U(cube):
    """
    arg: cube
    return: changed cube
    
    info: rotate cube as U
    side = [1, 5, 3, 0] # 0 -> 3 -> 5 -> 1
    ind = [0, 1, 2]
    rside = 2
    """
    side = [1, 5, 3, 0] # 0 -> 3 -> 5 -> 1
    ind = [0, 1, 2]
    rside = 2
    cube = rotate_cube(cube, side, ind, rside)

    return cube 

def L(cube):
    """
    arg: cube
    return: changed cube
    
    info: rotate cube as L
    side = [4, 5, 2, 0] # 0 -> 2 -> 5 -> 4
    ind = [0, 3, 6]
    rside = 1
    """
    side = [4, 5, 2, 0] # 0 -> 2 -> 5 -> 4
    ind = [0, 3, 6]
    rside = 1
    cube = rotate_cube(cube, side, ind, rside)

    return cube 

def B(cube):
    """
    arg: cube
    return: changed cube
    
    info: rotate cube as B
    side = [3, 4, 1, 2] # 2 -> 1 -> 4 -> 3
    ind = [0, 1, 2]
    rside = 0
    """
    side = [3, 4, 1, 2] # 2 -> 1 -> 4 -> 3
    ind = [0, 1, 2]
    rside = 0
    cube = rotate_cube(cube, side, ind, rside)

    return cube 

def D(cube):
    """
    arg: cube
    return: changed cube
    
    info: rotate cube as D
    side = [3, 5, 1, 0] # 0 -> 1 -> 5 -> 3
    ind = [6, 7, 8]
    rside = 4
    """
    side = [3, 5, 1, 0] # 0 -> 1 -> 5 -> 3
    ind = [6, 7, 8]
    rside = 4
    cube = rotate_cube(cube, side, ind, rside)

    return cube 

def rotate_side(side, rlist):
    new = []
    for i in range(len(side)):
        new.append(side[rlist[i]])
    
    return new

def rotate_cube(cube, side, ind, rside):
    """
    arg: cube, side, ind, rside
    return: changed cube
    info: rotate cube for all
    """

    """

    #違う面に移動する処理
    ind = [6, 7, 8]
    side: 1 -> 2 -> 3 -> 4
    side = [4, 3, 2, 1] 逆順
    
    kari = l[4]
    l[4] = l[3]
    l[3] = l[2]
    l[2] = l[1]
    l[1] = ( l[4] )

    #同じ面で回転する処理
    012  -->  630
    345  -->  741
    678  -->  852
    [6, 3, 0, 7, 4, 1, 8, 5, 2]

    """

    kari = []

    # set first to kari
    kari = tuple(cube[side[0]])
    
    # swap
    for i in range(0, len(side)-1, 1):
        for j in ind:
            cube[side[i]][j] = str(cube[side[i+1]][j])
    
    # set last from kari
    for i in ind:
        cube[side[3]][i] = str(kari[i])
    
    # rotate side
    rlist = [6, 3, 0, 7, 4, 1, 8, 5, 2]
    cube[rside] = rotate_side(cube[rside], rlist)
    return cube

def flex(cube, r):

    rlist = ['R', 'F', 'U', 'L', 'B', 'D']
    six_side = [[2, 5, 4, 0], [4, 3, 2, 1], [1, 5, 3, 0], [4, 5, 2, 0], [3, 4, 1, 2], [3, 5, 1, 0]]
    six_ind = [[2, 5, 8], [6, 7, 8], [0, 1, 2], [0, 3, 6], [0, 1, 2], [6, 7, 8]]
    six_rside = [3, 5, 2, 1, 0, 4]

    side = list()
    ind = list()
    rside = int()

    for i in range(len(rlist)):
        if r == rlist[i]:
            side = six_side[i]
            ind = six_ind[i]
            rside = six_rside[i]
    
    cube = rotate_cube(cube, side, ind, rside)
    return cube

