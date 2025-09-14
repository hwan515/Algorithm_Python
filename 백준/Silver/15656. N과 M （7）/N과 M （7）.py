def backtracking():
    if len(result) == M:
        print(*result)
        return

    for i in range(N):
        result.append(arr[i])
        backtracking()
        result.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []
backtracking()