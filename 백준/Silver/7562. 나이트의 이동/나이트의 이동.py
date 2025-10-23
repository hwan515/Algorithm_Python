from collections import deque
def bfs(si, sj, cnt):
    q = deque([(si, sj, cnt)])
    visited = set()
    visited.add((si, sj))
    directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

    while q:
        i, j, c= q.popleft()

        if i == ei and j == ej:
            return c

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < l and 0 <= nj < l and (ni, nj) not in visited:
                q.append((ni, nj, c + 1))
                visited.add((ni, nj))



T = int(input())
for _ in range(T):
    l = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    print(bfs(si, sj, 0))