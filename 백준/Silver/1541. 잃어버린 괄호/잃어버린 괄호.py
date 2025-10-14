expression = input().split('-')

result = 0
for i in range(len(expression)):
    k = expression[i].split('+')
    curr_total = 0
    for num in k:
        curr_total += int(num)
    if i == 0:
        result += curr_total
    else:
        result -= curr_total

print(result)