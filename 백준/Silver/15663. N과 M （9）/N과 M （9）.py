def backtracking():
    if len(result) == M:
        print(*result)
        return

    remember = 0

    for i in range( N):
        if visited[i] == 0 and remember != arr[i]:
            visited[i] = 1
            result.append(arr[i])
            remember = arr[i]
            backtracking()
            visited[i] = 0
            result.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [0] * N

result = []
backtracking()