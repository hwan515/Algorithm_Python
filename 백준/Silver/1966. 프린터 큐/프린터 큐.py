from collections import deque
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    q = deque([])
    for i in range(N):
        q.append((arr[i], i))
    arr = sorted(arr, reverse=True)

    cnt = 0

    while True:
        num, idx = q.popleft()
        if num < arr[0]:
            q.append((num, idx))

        # 출력
        elif num == arr[0]:
            cnt += 1
            arr.pop(0)
            if idx == M:
                break
    print(cnt)