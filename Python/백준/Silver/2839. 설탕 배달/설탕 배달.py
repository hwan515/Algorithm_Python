N = int(input())

ans = -1
if N % 5 == 0:
    ans = N // 5
else:
    cnt = 0
    while N > 0:
        N -= 3
        cnt += 1
        if N % 5 == 0:
            cnt += N//5
            ans = cnt
            break
        elif N == 1 or N == 2:
            break
        elif N == 0:
            ans = cnt
print(ans)