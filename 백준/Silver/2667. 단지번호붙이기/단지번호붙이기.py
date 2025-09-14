from collections import deque
def bfs(si, sj):
    q = deque([(si, sj)])
    visited[si][sj] = True

    cnt = 1
    while q:
        i, j = q.popleft()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and map[ni][nj] == 1:
                visited[ni][nj] = True
                cnt += 1
                q.append((ni, nj))
    result.append(cnt)

N = int(input())
map = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
result = []

for i in range(N):
    for j in range(N):
        if  not visited[i][j] and map[i][j] == 1:
            bfs(i, j)
result.sort()
print(len(result))
for cnt in result:
    print(cnt)