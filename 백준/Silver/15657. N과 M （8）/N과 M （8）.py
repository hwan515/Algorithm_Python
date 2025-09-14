def backtracking(idx):
    if len(result) == M:
        print(*result)
        return

    for i in range(idx, N):
        result.append(arr[i])
        backtracking(i)
        result.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []
backtracking(0)