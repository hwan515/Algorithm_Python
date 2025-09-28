from heapq import heappop, heappush
import sys 

input = sys.stdin.readline

T = int(input())
pq = []
for _ in range(T):
    N = int(input())
    if N == 0:
        if pq:
            print(-heappop(pq))
        else:
            print(0)
    else:
        heappush(pq, -N)
