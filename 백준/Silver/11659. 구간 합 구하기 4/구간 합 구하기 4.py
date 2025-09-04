N, M = map(int, input().split())
nums = list(map(int, input().split()))
my_sum = 0
sum_lst = [0]

for i in range(N):
    my_sum += nums[i]
    sum_lst.append(my_sum)

for _ in range(M):
    s, e = map(int, input().split())
    result = sum_lst[e] - sum_lst[s-1]
    print(result)