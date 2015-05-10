def findNextCellToFill(grid: arr, i, j):
    while i < 9:
        while j < 9:
            if(grid[i*j] == 0):
                return([i, j], items=2)
    x = 0
    y = 0
    while x < 9:
        while y < 9:
            if(grid[x*y] == 0):
                return([x, y], items=2)
    return([-1, -1], items=2)

def isValid(grid: arr, i, j, e):
    x = 0
    while x < 9:
        if(e == grid[i*x] || e==grid[j*x]):
            return(0)
    # finding the top left x,y co-ordinates of the section containing the i,j cell
    secTopX = 3 *(i/3)
    secTopY = 3 *(j/3)
    x = secTopX
    y = secTopY
    while x < secTopX + 3:
        while y < secTopY + 3:
            if(grid[x*y] == e):
                return(0)
    return(1)

def solveSudoku(grid: arr, i, j):
    ij = self.findNextCellToFill(grid, i, j, outsz=2)
    if ij[0] == -1:
        return(1) 
    e = 1
    while e < 10:
        if self.isValid(grid,i,j,e):
            grid[i*j] = e
            if self.solveSudoku(grid, i, j):
                return(1)
            # Undo the current cell for backtracking
            grid[i*j] = 0
        e += 1
    return(0)