from collections import deque
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def bfs(si, sj):
    q = deque([(si, sj)])
    visited[si][sj] = True
    directions = [(1, 0), (0, 1)]

    while q:
        i, j = q.popleft()
        can_go = graph[i][j]

        if graph[i][j] == -1:
            return True

        for di, dj in directions:
            ni, nj = i + di * can_go, j + dj * can_go
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj))

    return False

result = bfs(0, 0)

if result:
    print("HaruHaru")
else:
    print("Hing")