S = input()
lower = [chr(c) for c in range(ord('a'), ord('z')+1)]

for ch in lower:
    if ch in S:
        print(S.index(ch), end=' ')
    else:
        print(-1, end=' ')
