N = int(input())
nums = list(map(int, input().split()))
set_nums = sorted(list(set(nums)))
dict_num = {}
for n in range(len(set_nums)):
    dict_num[set_nums[n]] = n

result = [0] * N
for i in range(N):
    result[i] = dict_num[nums[i]]

print(*result)