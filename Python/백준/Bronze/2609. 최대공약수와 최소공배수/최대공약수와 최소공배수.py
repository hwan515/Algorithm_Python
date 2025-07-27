# 백준 2609
N, M = map(int, input().split())

for i in range(min(N, M), 0, -1):
    if N % i == 0 and M % i == 0:
        print(i)
        print(int(N*M/i))
        break