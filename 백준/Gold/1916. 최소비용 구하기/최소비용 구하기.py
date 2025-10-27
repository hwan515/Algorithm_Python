from heapq import heappop, heappush
def dijkstra(start_node, end_node):
    pq = []
    heappush(pq, (0, start_node))
    costs = [21e8] * (N + 1)
    costs[start_node] = 0

    while pq:
        cost, node = heappop(pq)

        if cost > costs[node]:
            continue

        for curr_cost, next_node in graph[node]:
            next_cost = cost + curr_cost

            if next_cost >= costs[next_node]:
                continue

            costs[next_node] = next_cost
            heappush(pq, (next_cost, next_node))

    return costs[end_node]

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
sn, en = map(int, input().split())

print(dijkstra(sn, en))