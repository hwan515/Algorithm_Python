def prime_num(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
try:
    N = int(input())
    numbers = list(map(int, input().split()))
    prime_count = 0
    for num in numbers:
        if prime_num(num):
            prime_count += 1
    print(prime_count)
except Exception as e:
    print(f"예상치 못한 오류가 발생했다: {e}")    
