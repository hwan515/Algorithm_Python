arr = []
for _ in range(10):
    n = int(input())
    k = n % 42
    arr.append(k)
print(len(set(arr)))