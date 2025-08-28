from collections import deque

def dfs(start, dfs_visited):
    dfs_visited[start] = True
    for nxt in sorted(graph[start]):
        if not dfs_visited[nxt]:
            dfs_visited[nxt] = True
            dfs_arr.append(nxt)
            dfs(nxt, dfs_visited)

def bfs(start):
    q = deque([start])
    visited = [False] * (N+1)
    visited[start] = True
    bfs_arr = [start]

    while q:
        now = q.popleft()
        for nxt in sorted(graph[now]):
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                bfs_arr.append(nxt)
    print(*bfs_arr)


N, M, start = map(int, input().split())
graph = [[] for _ in range(N+1)]
dfs_arr = []
dfs_visited = [False] * (N+1)

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

dfs_arr.append(start)
dfs(start, dfs_visited)
print(*dfs_arr)

bfs(start)