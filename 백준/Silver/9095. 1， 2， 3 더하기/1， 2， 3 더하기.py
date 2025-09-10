def solve(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        dp[n] = solve(n-1) + solve(n-2) + solve(n-3)
        return dp[n]


T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0] * 12
    print(solve(N))