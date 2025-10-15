K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    result = 0
    for l in arr:
        result += l // mid
    if result >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)