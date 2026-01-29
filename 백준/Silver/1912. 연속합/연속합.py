n = int(input())
arr = list(map(int, input().split()))

cur = arr[0]
best = arr[0]
for x in arr[1:]:
    cur = max(x, cur + x)
    best = max(best, cur)

print(best)