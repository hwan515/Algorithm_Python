def solve(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        half = solve(a, b // 2, c)
        return (half * half) % c
    else:
        half = solve(a, (b - 1) // 2, c)
        return (half * half * a) % c

a, b, c = map(int, input().split())

print(solve(a, b, c))