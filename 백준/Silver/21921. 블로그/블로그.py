N, M = map(int, input().split())
arr = list(map(int, input().split()))


total = 0

for i in range(M):
    total += arr[i]

max_total = total
day_cnt = 1

for t in range(M, N):
    total += arr[t]

    total -= arr[t-M]

    if max_total < total:
        max_total = total
        day_cnt = 1
    elif max_total == total:
        day_cnt += 1

if max_total == 0:
    print('SAD')
else:
    print(max_total)
    print(day_cnt)