N, K = map(int, input().split())

def factorial(num):
    if num <= 1:
        return 1
    return factorial(num-1) * num

result = factorial(N)//(factorial(N - K) * factorial(K))
print(result)