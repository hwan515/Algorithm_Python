N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * i for i in range(1, N + 1)]
dp[0] = arr[0]

for i in range(1, N):
    for j in range(len(arr[i])):
        # i - 1행 idx(j)가 맨끝일때
        if j == len(arr[i]) - 1:
            dp[i][j] = dp[i - 1][j - 1] + arr[i][j]
        # i - 1행 idx(j)가 0일때
        elif j == 0:
            dp[i][j] = dp[i - 1][j] + arr[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + arr[i][j]

print(max(dp[-1]))