# 백준 2231 
N = int(input())

result = 0
# 1,000,000 이하 자연수 임으로 54 (9*6 = 54)이하의 작은 수 부터 계산하면 최적화를 할 수 있다.
# 음수 일때를 대비하여 max 함수를 이용하여 54보다 작을때 대비
for num in range(max(1, N-54), N+1):
    sum_of_digit = sum(map(int, str(num)))
    
    total = sum_of_digit + num
    
    if total == N:
        result = num
        break

print(result)