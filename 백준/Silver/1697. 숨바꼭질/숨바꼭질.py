from collections import deque
N, K = map(int, input().split())
cnt = 0

def bfs(start_num, cnt):

    q = deque([(start_num, cnt)])
    visited = set()

    while q:
        num, count = q.popleft()
        operation = (num - 1, num + 1, num * 2)
        for next_num in operation:
            if 0 <= next_num <= 100000 and next_num not in visited:
                if next_num == K:
                    return count + 1
                visited.add(next_num)
                q.append((next_num, count + 1))
if N == K:
    print(0)
else:
    print(bfs(N, cnt))