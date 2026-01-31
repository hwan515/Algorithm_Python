from collections import deque

def bfs(si, sj):
    q = deque([(si, sj)])
    directions = [[-1, 0], [1, 0], [0, -1], [0 ,1]]
    while q:
        i, j = q.popleft()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and answer[ni][nj] == -1 and matrix[ni][nj] != 0:
                answer[ni][nj] = answer[i][j] + 1
                q.append((ni, nj))

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = [[-1] * m for _ in range(n)]

found = False
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            answer[i][j] = 0
            bfs(i, j)
            found = True
            break
    if found:
        break

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            answer[i][j] = 0

for row in answer:
    print(*row)

