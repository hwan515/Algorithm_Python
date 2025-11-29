import sys
input = sys.stdin.readline
write = sys.stdout.write

M = int(input())
S = set()

for _ in range(M):
    parts = input().split()
    cmd = parts[0]

    if cmd == 'add':
        x = int(parts[1])
        S.add(x)

    elif cmd == 'remove':
        x = int(parts[1])
        S.discard(x)

    elif cmd == 'check':
        x = int(parts[1])
        if x in S:
            write('1\n')
        else:
            write('0\n')

    elif cmd == 'toggle':
        x = int(parts[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)

    elif cmd == 'all':
        S = set(range(1, 21))

    elif cmd == 'empty':
        S = set()
