N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []

def backtracking():
    if len(ans) == M:
        result = ' '.join(map(str, ans))
        print(result)
        return

    for i in arr:
        if i not in ans:
            ans.append(i)
            backtracking()
            ans.pop()

backtracking()