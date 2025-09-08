N = int(input())
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append([s, e])
arr.sort(key = lambda x: (x[1], x[0]))

cnt = 0
end_time = 0
for i in range(N):
    if arr[i][0] >= end_time:
        cnt += 1
        end_time = arr[i][1]

print(cnt)