from collections import deque
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

def bfs(start):
    q = deque([start])
    visited = [0 for _ in range(N)]

    while q:
        node = q.popleft()

        for i in range(N):
            if visited[i] == 0 and matrix[node][i] == 1:
                q.append(i)
                visited[i] = 1
                matrix[start][i] = 1

for i in range(N):
    bfs(i)

for r in matrix:
    print(*r)