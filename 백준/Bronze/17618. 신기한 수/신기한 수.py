# 신기한 수를 계산하는 함수
def is_mysterious_number(num):
    # num의 각 자릿수를 리스트로 변환한 후 합계 계산
    digit_sum = sum(map(int, str(num)))
    
    # 자릿수 합으로 나누어 떨어지면 True 반환
    return num % digit_sum == 0

# N 이하의 신기한 수의 개수를 계산하는 함수
def count_mysterious_numbers(N):
    count = 0
    for i in range(1, N + 1):
        if is_mysterious_number(i):
            count += 1
    return count

N = int(input())

print(count_mysterious_numbers(N))