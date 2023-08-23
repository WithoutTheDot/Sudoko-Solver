# I got bored of sitting around for hours solving sudokus so why not get the computer to do it.



def is_valid_move(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
    for y in range(9):
        if grid[y][col] == num:
            return False
    
    corner_row = row-row % 3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row+x][corner_col+y] == num:
                return False
            
    return True

def solve(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col+1)
    
    for num in range(1,10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve(grid,row,col+1):
                return True
            
        grid[row][col] = 0

    return False

def get_user_grid():
    print("""
Usage:
        To use this enter the size of the sudoko 
        then the numbers with 0 being empty from left to right and downwards 
        (like reading a book)""")
    grid = []
    for i in range(9):
        line = []
        for j in range(9):
            line.append(int(input(f"Enter row {j} col {i}: ")))
        grid.append(line)
    return grid

grid =  get_user_grid() #Enter soduko here


if solve(grid, 0,0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end = "  ")
        print()
else:
    print("No solution found")
