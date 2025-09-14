def backtracking():
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            result.append(i)
            backtracking()
            visited[i] = 0
            result.pop()

N, M = map(int, input().split())
visited = [0] * (N+1)
result = []
backtracking()