dp = [0] * 100
dp[0] = 1
dp[1] = 1
dp[2] = 1

def solve(n):
    if dp[n] == 0:
        dp[n] = solve(n - 2) + solve(n - 3)
        return dp[n]
    else:
        return dp[n]
T = int(input())
for tc in range(T):
    N = int(input())
    print(solve(N - 1))