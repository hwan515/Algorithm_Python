from collections import deque
def bfs(start):

    q = deque([start])
    visited = [-1] * (N + 1)
    visited[start] = 0

    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + 1
                q.append(next_node)
    return sum(visited[1:N+1])

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
# print(graph)

min_sum = 10**15
person = -1
for start in range(1, N + 1):
    tmp_sum = bfs(start)
    if tmp_sum < min_sum:
        min_sum = tmp_sum
        person = start
print(person)