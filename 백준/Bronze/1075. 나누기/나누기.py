N = int(input())
M = int(input())

temp = (N // 100) * 100 

while temp % M != 0:
    temp += 1

print(str(temp)[-2:])