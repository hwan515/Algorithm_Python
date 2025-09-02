n = int(input())
sum_num = 0

for i in range(1, n+1):
    if n % i == 0:
        sum_num += i
final_num  = sum_num * 5 - 24

print(final_num)