N = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3

def solve(N):
    if dp[N] == 0:
        dp[N] = solve(N - 1) + 2 * solve(N - 2)
        return dp[N]
    else:
        return dp[N]

print(solve(N) % 10007)