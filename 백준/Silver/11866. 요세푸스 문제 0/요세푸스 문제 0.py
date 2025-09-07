N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]

result = []
while arr:
    for _ in range(K - 1):
        arr.append(arr.pop(0))
    result.append(arr.pop(0))
print('<', ', '.join([str(item) for item in result]), '>', sep='')