from start import initialize
from rotate import flex as rotate
from show import show_cube

# (012345) = (WOGRBY)
#  0  
# 1234
#  5  

# 012
# 345
# 678

# URL: https://cstimer.net

def main():
    scli = "D' L D' B2 L2 U' R2 D B2 L2 U F2 D L B F' R2 U B' R' B2"
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
        cube = rotate(cube, sc[0], ind)
        show_cube(cube)



def testcode():
    rlist = ['R', 'L', 'U', 'D', 'F', 'B']
    rind = [1, 2, 3]

    for w in rlist:
        for i in rind:
            print(f'(w, i) = ({w}, {i})')
            cube = initialize()
            cube = rotate(cube, w, i)
            show_cube(cube)

if __name__ == '__main__':
    main()