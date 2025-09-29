from heapq import heappush, heappop
pq = []
N = int(input())
for _ in range(N):
    oper = int(input())
    if oper:
        if oper < 0:
            heappush(pq, (-oper, -1))
        else:
            heappush(pq, (oper, 1))
    else:
        if not pq:
            print(0)
        else:
            oper, com = heappop(pq)
            if com < 0:
                print(-oper)
            else:
                print(oper)
