import sys
input = sys.stdin.readline

MAX = 40
zero = [0] * (MAX + 1)
one  = [0] * (MAX + 1)

# base
zero[0], one[0] = 1, 0
zero[1], one[1] = 0, 1

# 점화식: n>=2일 때, (0/1 출력 횟수) = (n-1) + (n-2)
for i in range(2, MAX + 1):
    zero[i] = zero[i-1] + zero[i-2]
    one[i]  = one[i-1]  + one[i-2]

T = int(input())
for _ in range(T):
    n = int(input())
    print(zero[n], one[n])