from collections import deque
import sys

input = sys.stdin.readline

def bfs(start):
    global cnt

    path = deque([start])
    visited[start] = True
    while path:
        now = path.popleft()
        for nxt in edges[now]:
            if not visited[nxt]:
                visited[nxt] = True
                path.append(nxt)
    # 순회가 종료 되면 연결 요소에 +1
    cnt += 1

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)

visited = [False] * (N+1)
cnt = 0
# 각 노드를 순회하면서 BFS 탐색
for node in range(1, N+1):
    # 해당 노드가 방문한적이 없다면
    if not visited[node]:
        bfs(node)

print(cnt)