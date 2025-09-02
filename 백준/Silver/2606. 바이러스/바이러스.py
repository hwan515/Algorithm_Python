from collections import deque

def bfs(start):
    # start번 컴퓨터는 방분 처리
    V = [False] * (N + 1)
    V[start] = True
    path = deque([start])
    cnt = 0

    while path:
        now = path.popleft()
        for nxt in edges[now]:
            if not V[nxt]:
                path.append(nxt)
                V[nxt] = True
                cnt += 1

    return cnt

N = int(input())
E = int(input())
# 경로 받아오기
edges = [[] for _ in range(N+1)]
for _ in range(E):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)

print(bfs(1))