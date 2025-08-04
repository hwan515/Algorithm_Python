T = int(input())
for _ in range(T):
    result = input()

    total = 0
    cnt = 0
    for i in result:
        if i == 'O':
            cnt += 1
            total += cnt
        else:
            cnt = 0

    print(total)
