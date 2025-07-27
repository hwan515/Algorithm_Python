A = int(input())
B = int(input())
C = int(input())

str_total = str(A * B * C)

for num in range(10):
    cnt = str_total.count(str(num))
    print(cnt)