import itertools

def get_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
houses = []
store = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            houses.append((i, j))
        elif matrix[i][j] == 2:
            store.append((i, j))

store_combinations = list(itertools.combinations(store, M))

min_total_dist = 21e8
for current_stores in store_combinations:
    city_dist = 0
    for house in houses:
        min_dist = 21e8
        for store in current_stores:
            dist = get_distance(house[0], house[1], store[0], store[1])
            min_dist = min(min_dist, dist)
        city_dist += min_dist
    min_total_dist = min(min_total_dist, city_dist)

print(min_total_dist)