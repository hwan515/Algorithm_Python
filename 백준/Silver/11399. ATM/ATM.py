N = int(input())
arr = list(map(int, input().split()))
arr.sort()
tmp_sum = 0
my_arr = []
for i in range(N):
    tmp_sum += arr[i]
    my_arr.append(tmp_sum)
print(sum(my_arr))