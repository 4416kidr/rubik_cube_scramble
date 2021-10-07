import definition as defi
def initialize():
    """
    set cube color
    arg: None
    return: color seted cube
    """
    cube = []
    dcolor = tuple(defi.color())
    for i in range(len(dcolor)):
        side = set_side(dcolor[i])
        cube.append(side)
    return cube

def set_side(color):
    """
    arg: color
    return: side of list
    """
    li = []
    for i in range(9):
        li.append(color + str(i))
    return li



