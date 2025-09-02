N = int(input())
lst = []
for i in range(N):
    age, name = input().split()
    lst.append([i, int(age), name])

lst.sort(key=lambda x: (x[1], x[0]))

for m in lst:
    print(m[1], m[2])