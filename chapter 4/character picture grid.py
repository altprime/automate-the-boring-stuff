'''
character grid

INPUT
grid = [[...]]

OUTPUT
..OO.OO.. 
.OOOOOOO. 
.OOOOOOO. 
..OOOOO.. 
...OOO... 
....O....
'''
grid = [['.', '.', '.', '.', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['.', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.']]

print('\n'.join(map(''.join, zip(*grid))))

#import numpy as np
#print ('\n'.join(''.join(str(cell) for cell in row) for row in np.array(grid).transpose()))
