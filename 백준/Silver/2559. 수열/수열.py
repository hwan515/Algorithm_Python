N, K = map(int, input().split())
temps = list(map(int, input().split()))

sum_temp = sum(temps[:K])
max_temp = sum_temp
for i in range(K, N):
    sum_temp += temps[i] - temps[i - K] # 새로 들어온 값 더하고, 빠지는 값 빼기
    if max_temp < sum_temp:
        max_temp = sum_temp

print(max_temp)