M, N = map(int, input().split())
prime_nums = []
for num in range(M, N+1):
    # 1은 소수가 아님
    if num == 1:
        continue

    prime_num = True
    for k in range(2, int(num ** (1/2)) + 1):
        if num % k == 0:
            prime_num = False
            break

    if prime_num:
        prime_nums.append(num)

for pn in prime_nums:
    print(pn)