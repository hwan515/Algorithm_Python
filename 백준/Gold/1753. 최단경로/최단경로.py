from heapq import heappop, heappush

def dijkstra(start_node):
    pq = []
    heappush(pq, (0, start_node))
    weights = [INF] * (V + 1)
    weights[start_node] = 0

    while pq:
        weight, node = heappop(pq)

        if weight > weights[node]:
            continue


        for curr_weight, next_node in graph[node]:
            next_weight = weight + curr_weight

            if next_weight <= weights[next_node]:
                weights[next_node] = next_weight
                heappush(pq, (next_weight, next_node))

    return weights


V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
INF = int(21e8)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

routes = dijkstra(K)

for n in range(1, len(routes)):
    if routes[n] == INF:
        print('INF')
    else:
        print(routes[n])