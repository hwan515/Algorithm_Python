def solution(n):
    for answer in range(2, n):
        if n % answer == 1:
            return answer
