def backtracking(idx):
    if len(result) == M:
        print(*result)
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            result.append(arr[i])
            backtracking(i + 1)
            visited[i] = 0
            result.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [0] * N
result = []
backtracking(0)