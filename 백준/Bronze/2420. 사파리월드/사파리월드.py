N, M = map(int, input().split())
if N < 0 or M < 0:
    if N-M < 0:
        print(M-N)
    else:
        print(N-M)
elif N == 0 and M == 0:
    print(0)
else:
    if N < M:
        print(M-N)
    else:
        print(N-M)