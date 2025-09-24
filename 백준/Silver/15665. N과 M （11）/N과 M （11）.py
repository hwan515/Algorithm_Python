N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

arr = []
visited = set()

def recur():
    if len(arr) == M:
        tuple_set = tuple(arr)
        if tuple_set not in visited:
            visited.add(tuple_set)
            print(*arr)
        return

    for i in range(N):
        arr.append(nums[i])
        recur()
        arr.pop()
recur()