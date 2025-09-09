from collections import deque
def bfs(si, sj):
    q = deque([(si, sj)])
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    matrix[si][sj] = 0
    visited[si][sj] = True
    while q:
        i, j = q.popleft()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and matrix[ni][nj] == 1:
                matrix[ni][nj] = matrix[i][j] + 1
                visited[ni][nj] = True
                q.append((ni, nj))


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

found = False
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            bfs(i, j)
            found = True
            break
    if found:
        break

# 다시 결과를 순회하면서 1을 -1로 변환
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and not visited[i][j]:
            matrix[i][j] = -1

for row in matrix:
    print(*row)