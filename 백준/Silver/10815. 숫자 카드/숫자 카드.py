N = int(input())
arr1 = set(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

result = [0] * M
for i in range(M):
    if arr2[i] in arr1:
        result[i] = 1

print(' '.join(map(str, result)))