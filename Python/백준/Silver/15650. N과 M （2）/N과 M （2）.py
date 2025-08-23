import sys
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
arr = []

def backtracking():
    if len(arr) == M:
        result = ' '.join(map(str, arr))
        print(result)
        return

    for i in range(1, N+1):
        if not arr or i > arr[-1]:
            arr.append(i)
            backtracking()
            arr.pop()

backtracking()