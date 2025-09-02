N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

dict = {}
for i in arr1:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

result = []
for j in arr2:
    if j in dict:
        result.append(dict[j])
    else:
        result.append(0)

print(*result)