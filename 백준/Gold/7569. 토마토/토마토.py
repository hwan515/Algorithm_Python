from collections import deque
M, N, H = map(int, input().split())
matrix3 = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False]*M for _ in range(N)] for _ in range(H)]
directions = [[1, 0, 0], [-1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]

result = 0

q = deque([])

for h in range(H):
    for n in range(N):
        for m in range(M):
            if matrix3[h][n][m] == 1:
                q.append((h, n, m))

while q:
    h, i, j = q.popleft()
    visited[h][i][j] = True
    for dh, di, dj in directions:
        nh, ni, nj = h + dh, i + di, j + dj
        if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and not visited[nh][ni][nj] and matrix3[nh][ni][nj] == 0:
            visited[nh][ni][nj] = True
            matrix3[nh][ni][nj] = matrix3[h][i][j] + 1
            result = max(matrix3[nh][ni][nj], result)
            q.append((nh, ni, nj))

found_0 = False
for h in range(H):
    for n in range(N):
        for m in range(M):
            if matrix3[h][n][m] == 0:
                result = -1
                found_0 = True
                break
        if found_0:
            break
    if found_0:
        break

if result > 0:
    print(result-1)
else:
    print(result)
