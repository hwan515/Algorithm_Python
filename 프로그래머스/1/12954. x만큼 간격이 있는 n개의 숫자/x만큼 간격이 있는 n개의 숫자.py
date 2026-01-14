def solution(x, n):
    answer = []
    for i in range(1, n+1):
        tmp = i * x
        answer.append(tmp)
    return answer