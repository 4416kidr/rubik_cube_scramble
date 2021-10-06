import simplify_rotate as sr

two = 2
prime = 3


def Ro(cube, ind):
    for i in range(ind):
        cube = sr.R(cube)
    return cube

def R(cube):
    return Ro(cube, 1)

def R2(cube):
    return Ro(cube, 2)

def Rp(cube):
    return Ro(cube, 3)


def Lo(cube, ind):
    for i in range(ind):
        cube = sr.L(cube)
    return cube

def L(cube):
    return Lo(cube, 1)

def L2(cube):
    return Lo(cube, 2)

def Lp(cube):
    return Lo(cube, 3)


def Uo(cube, ind):
    for i in range(ind):
        cube = sr.U(cube)
    return cube

def U(cube):
    return Uo(cube, 1)

def U2(cube):
    return Uo(cube, 2)

def Up(cube):
    return Uo(cube, 3)


def Do(cube, ind):
    for i in range(ind):
        cube = sr.D(cube)
    return cube

def D(cube):
    return Do(cube, 1)

def D2(cube):
    return Do(cube, 2)

def Dp(cube):
    return Do(cube, 3)


def Fo(cube, ind):
    for i in range(ind):
        cube = sr.F(cube)
    return cube

def F(cube):
    return Fo(cube, 1)

def F2(cube):
    return Fo(cube, 2)

def Fp(cube):
    return Fo(cube, 3)


def Bo(cube, ind):
    for i in range(ind):
        cube = sr.B(cube)
    return cube

def B(cube):
    return Bo(cube, 1)

def B2(cube):
    return Bo(cube, 2)

def Bp(cube):
    return Bo(cube, 3)


def rotate(cube, r, ind):
    if r == 'R':
        for i in range(1, 4, 1):
            if ind == i:
                cube = Ro(cube, i)
    elif r == 'L':
        for i in range(1, 4, 1):
            if ind == i:
                cube = Lo(cube, i)
    
    elif r == 'U':
        for i in range(1, 4, 1):
            if ind == i:
                cube = Uo(cube, i)
    elif r == 'D':
        for i in range(1, 4, 1):
            if ind == i:
                cube = Do(cube, i)
    
    elif r == 'F':
        for i in range(1, 4, 1):
            if ind == i:
                cube = Fo(cube, i)
    elif r == 'B':
        for i in range(1, 4, 1):
            if ind == i:
                cube = Bo(cube, i)

    else:
        print('ERROR')

    return cube

def flex(cube, r, ind):
    for i in range(ind):
        cube = sr.flex(cube, r)
    return cube
