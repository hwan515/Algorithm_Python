N = int(input())
arr = []
# print(arr)
for _ in range(N):
    v = int(input())
    arr.append(v)
arr.sort()

for i in arr:
    print(i)