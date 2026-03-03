N = int(input())
T = [0] * (N + 2)
P = [0] * (N + 2)

for i in range(1, N + 1):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

dp = [0] * (N + 2)

for i in range(1, N + 1):
    # 상담하지 않으면 다음으로 넘김
    dp[i + 1] = max(dp[i + 1], dp[i])

    # 상담을 하면
    # 다음 상담을 할 수 있는 날짜는 현재 날짜(i) + 걸리는 시간(T[i])
    end = i + T[i]
    if end < N + 2:
        dp[end] = max(dp[end], dp[i] + P[i])

print(dp[N + 1])