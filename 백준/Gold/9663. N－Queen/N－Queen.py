def is_safe(row):
    for i in range(row):
        if board[i] == board[row] or abs(board[row] - board[i]) == row - i:
            return False
    return True

def backtracking(row):
    global result
    if row == N:
        result += 1
        return

    for col in range(N):
        board[row] = col
        if is_safe(row):
            backtracking(row + 1)

N = int(input())
board = [0] * N 
result = 0
backtracking(0)
print(result)