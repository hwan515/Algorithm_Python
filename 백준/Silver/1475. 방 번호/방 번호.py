n = input()
num_set = [0] * 10

for i in n:
    num_set[int(i)] += 1

tmp_num = num_set[6] + num_set[9]
if tmp_num % 2 == 0:
    tmp_num //= 2
else:
    tmp_num = tmp_num // 2 + 1
num_set[6] = tmp_num
num_set[9] = tmp_num

answer = max(num_set)

print(answer)