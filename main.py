grid = [
    [4, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 9, 8],
    [3, 0, 0, 0, 8, 2, 4, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 8, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 6, 7, 0],
    [0, 5, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 9, 0, 7],
    [6, 4, 0, 3, 0, 0, 0, 0, 0],
]

def solveSudoku(board):
    solveSudokuHelper(0,0,board)

def solveSudokuHelper(x,y,board):

    # this happens when the board is solved
    if x == 8 and y == 8:
        if board[y][x]!=0:
            for row in board:
                for ele in row:
                    print(ele, end=" ")
                print()
        else:
            for i in range(1,10):
                if isValid(x,y,i,board) is True:
                    board[y][x]=x
                    for row in board:
                        for ele in row:
                            print(ele, end=" ")
                        print()
                    board[y][x]=0
        print()
        return


    # this happens when the board is at the final row, and needs to go down a row
    if x>8:
        solveSudokuHelper(0,y+1,board)  
        return

    if board[y][x] == 0:
        for i in range(1,10):
            if isValid(x, y, i, board):
                board[y][x] = i
                solveSudokuHelper(x+1, y, board)
                board[y][x] = 0
    else:
        solveSudokuHelper(x+1, y, board)

    return


def isValid(x, y, num, grid):

    # row checking
    if num in grid[y]:
        return(False)
    
    # column checking
    for row in range(9):
        if num == grid[row][x]:
            return(False)

    # square checking
    startRow = y - (y % 3)
    startCol = x - (x % 3)

    row = startRow
    while row <= startRow + 2:
        col = startCol
        while col <= startCol + 2:
            if grid[row][col] == num:
                return(False)
            col += 1
        row += 1

    return(True)

if __name__ == "__main__":
    print(solveSudoku(grid))