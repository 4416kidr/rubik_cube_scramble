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



rlist = ['R', 'L', 'U', 'D', 'F', 'B']
rind = [1, 2, 3]

for w in rlist:
    for i in rind:
        cube = initialize()
        cube = r.flex(cube, w, i)
        print(f'(w, i) = ({w}, {i})')
        show_cube(cube)
