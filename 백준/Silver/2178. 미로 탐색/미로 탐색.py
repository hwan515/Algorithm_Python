from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

def bfs():

    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = [[False] * M for _ in range(N)]
    q = deque([(0, 0, 1)])
    visited[0][0] = True

    while q:
        i, j, d = q.popleft()
        if i == N - 1 and j == M - 1:
            return d

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and maze[ni][nj] == 1:
                visited[ni][nj] = True
                q.append((ni, nj, d+1))

print(bfs())