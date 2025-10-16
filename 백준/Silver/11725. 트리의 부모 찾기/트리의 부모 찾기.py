
from collections import deque

N = int(input())
edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)
    
result = [-1] * (N + 1)

def bfs(start_node):
    q = deque([start_node])
    result[start_node] = 0

    while q:
        n = q.popleft()
        for nn in edges[n]:
            if result[nn] == -1:
                result[nn] = n
                q.append(nn)
bfs(1)
for i in range(2, len(result)):
    print(result[i])