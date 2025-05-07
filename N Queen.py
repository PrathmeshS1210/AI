#N Queen
def solve(board, row):
    if row == n:
        for r in board: print(' '.join(r))
        print('-' * 10)
        return
    for col in range(n):
        if all(board[i][col] != 'Q' and 
               (row - i != abs(col - c) or board[i][c] != 'Q') 
               for i in range(row) for c in range(n)):
            board[row][col] = 'Q'
            solve(board, row + 1)
            board[row][col] = '.'

n = int(input("Board size: "))
board = [['.'] * n for _ in range(n)]
solve(board, 0)
