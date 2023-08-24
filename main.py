# I got bored of sitting around for hours solving sudokus so why not get the computer to do it.



def is_valid_move(grid, row, col, num, size):
    for x in range(size):
        if grid[row][x] == num:
            return False
    for y in range(size):
        if grid[y][col] == num:
            return False
    
    corner_row = row-row % int(size**(1/2))
    corner_col = col - col % int(size**(1/2))
    for x in range(int(size**(1/2))):
        for y in range(int(size**(1/2))):
            if grid[corner_row+x][corner_col+y] == num:
                return False
            
    return True

def solve(grid, row, col, size):
    if col == size:
        if row == size-1:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col+1, size)
    
    for num in range(1,size):
        if is_valid_move(grid, row, col, num, size):
            grid[row][col] = num
            if solve(grid,row,col+1, size):
                return True
            
        grid[row][col] = 0

    return False

def get_user_grid():
    print("""
Usage:
        To use this enter the size of the sudoko 
        then the numbers with 0 being empty from left to right and downwards 
        (like reading a book)""")
    size = int(input("Size of the sudoko: "))
    grid = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(int(input(f"Enter col {i} row {j}: ")))
        grid.append(line)
    return grid, size

grid, size =  get_user_grid() #Enter soduko here

for i in grid:
    print(i)
if solve(grid, 0,0, size):
    for i in range(size):
        for j in range(size):
            print(grid[i][j], end = "  ")
        print()
else:
    print("No solution found")
