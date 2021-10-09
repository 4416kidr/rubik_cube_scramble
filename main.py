from start import initialize
import start as st
import rotate as r
from show import show_cube

"""
 0  
1234
 5  

012
345
678

"""


scli = "B2 D' L2 F2 B D2 F' U D B D' R2 B2 L' U2 R2 B2 L2"
scli = scli.split(' ')

cube = initialize()
for sc in scli:
    ind = -1
    if len(sc) != 1:
        if sc[1] == "'":
            ind = 3
        elif sc[1] == '2':
            ind = 2
    elif len(sc) == 1:
        ind = 1
    cube = r.flex(cube, sc[0], ind)
    show_cube(cube)



def testcode():
    rlist = ['R', 'L', 'U', 'D', 'F', 'B']
    rind = [1, 2, 3]

    for w in rlist:
        for i in rind:
            print(f'(w, i) = ({w}, {i})')
            cube = initialize()
            cube = r.flex(cube, w, i)
            show_cube(cube)