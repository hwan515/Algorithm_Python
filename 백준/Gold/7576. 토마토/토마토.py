def bfs():
    while well:
        i, j = well.popleft()
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == 0:
                matrix[ni][nj] = matrix[i][j] + 1
                well.append((ni, nj))
    max_num = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                return -1
            else:
                if matrix[i][j] > max_num:
                    max_num = matrix[i][j]
    if max_num == 1:
        return 0
    return max_num - 1


from collections import deque
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
well = deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            well.append((i, j))

print(bfs())