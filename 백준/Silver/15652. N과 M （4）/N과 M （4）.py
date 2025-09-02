N, M = map(int, input().split())
arr = []

def backtracking(num):
    if len(arr) == M:
        result = ' '.join(map(str, arr))
        print(result)
        return

    for i in range(num, N+1):
        arr.append(i)
        backtracking(i)
        arr.pop()

backtracking(1)