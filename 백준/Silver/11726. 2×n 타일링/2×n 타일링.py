import sys

n = int(sys.stdin.readline())

# DP 테이블 초기화
dp = [0] * 1001

# 초기값 설정
dp[1] = 1
dp[2] = 2

# 점화식을 이용해 DP 채우기
for i in range(3, n + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])