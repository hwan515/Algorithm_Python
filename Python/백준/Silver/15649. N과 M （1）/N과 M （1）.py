def backtracking():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, N + 1):
        if i not in arr:
            arr.append(i)
            backtracking()
            arr.pop()

N, M = map(int, input().split())
arr = []

backtracking()