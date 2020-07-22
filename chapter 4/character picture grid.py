import numpy as np
grid = [['.', '.', '.', '.', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['.', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.']]

#print ('\n'.join(''.join(str(cell) for cell in row) for row in np.array(grid).transpose()))

print('\n'.join(map(''.join, zip(*grid))))
