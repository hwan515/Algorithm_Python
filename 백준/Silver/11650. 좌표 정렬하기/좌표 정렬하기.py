
T = int(input())
matrix = []
for _ in range(T):
    x, y = map(int, input().split())
    matrix.append([x, y])
matrix.sort()
for row in matrix:
    print(*row)