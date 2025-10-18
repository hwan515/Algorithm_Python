ISBN = list(input())
total = 0
star_idx = None
for num in range(13):
    if ISBN[num] == '*':
        star_idx = num
        continue
    if num % 2 == 0:
        total += int(ISBN[num])
    elif num % 2 != 0:
        total += int(ISBN[num]) * 3

weight = 1 if star_idx % 2 == 0 else 3

for x in range(10):
    if (total + x * weight) % 10 == 0:
        print(x)
        break