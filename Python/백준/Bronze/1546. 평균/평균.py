def calculate_average(scores):
    result = []
    for score in scores:
        new_score = (score/max(scores)) * 100
        result.append(new_score)
    return sum(result) / len(result)

N = int(input())
scores = list(map(int, input().split()))
print(calculate_average(scores))