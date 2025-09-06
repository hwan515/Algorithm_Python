
from collections import deque

def bfs(si, sj):
    q = deque([(si, sj)])
    visited[si][sj] = 1
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    cnt = 1
    while q:
        i, j = q.popleft()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1 and matrix[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1
    return cnt




N, M = map(int,input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

result = []

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and visited[i][j] == -1:
            cnt = bfs(i, j)
            result.append(cnt)
if len(result) == 0:
    print(0)
    print(0)
else:
    print(len(result))
    print(max(result))

