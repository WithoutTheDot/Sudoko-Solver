from tkinter import *
from solver import solver


root = Tk()
root.title("Sudoku Solver")
root.geometry("325x550")

label = Label(root, text="Fill in the numbers and click solve").grid(row=0, column=1, columnspan=10)

errLabel = Label(root, text="", fg="red")
errLabel.grid(row=15, column=1, columnspan=10, pady=5)

solvedLabel = Label(root, text="", fg="green")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)

cells = {}

def ValidateNumber(P):
    out = (P.isdigit() or P == "") and len(P)<2
    return out

reg = root.register(ValidateNumber)

def draw3x3Grid(row, col, bgcolour):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width=5, bg=bgcolour, justify="center", validate="key", validatecommand=(reg, "%P"))
            e.grid(row=row+i+1, column=col+j+1, sticky="nsew", padx=1, pady=1, ipady=5)
            cells[(row+i+1, col+j+1)] = e

def draw9x9Grid():
    colour = "#D0ffff"
    for rowNo in range(1,10,3):
        for colNo in range(0,9,3):
            draw3x3Grid(rowNo, colNo, colour)
            if colour == "#D0ffff":
                colour = "#ffffD0"
            else:
                colour = "#D0ffff"

def clearValues():
    errLabel.configure(text="")
    solvedLabel.config(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell = cells[(row, col)]
            cell.delete(0, "end")

def getValues():
    board = []
    errLabel.configure(text="")
    solvedLabel.config(text="")
    for row in range(2,11):
        rows = []
        for col in range(1,10):
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    updateValues(board)

btn = Button(root, command=getValues, text="Solve", width=10)
btn.grid(row=20, column=1, columnspan=5, pady=20)

btn = Button(root, command=clearValues, text="Clear", width=10)
btn.grid(row=20, column=5, columnspan=5, pady=20)
    
def updateValues(s):
    sol = solver(s)
    if sol != "no":
        for rows in range(2,11):
            for col in range(1,10):
                cells[(rows,col)].delete(0, "end")
                cells[(rows,col)].insert(0, sol[rows-2][col-1])
        solvedLabel.configure(text = "Sudoku Solved")
    else:
        errLabel.configure(text="No solution found")

draw9x9Grid()
root.mainloop()