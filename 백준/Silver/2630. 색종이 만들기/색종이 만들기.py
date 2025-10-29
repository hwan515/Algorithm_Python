def solve(i, j, n):
    global blue
    global white
    color = paper[i][j]
    for pi in range(i, i + n):
        for pj in range(j, j + n):
            if paper[pi][pj] != color:
                solve(i, j, n // 2)
                solve(i, j + n // 2, n // 2)
                solve(i + n // 2, j, n // 2)
                solve(i + n // 2, j + n // 2, n // 2)
                return
    if color == 1:
        blue += 1
    else:
        white += 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0
solve(0, 0, N)
print(white)
print(blue)