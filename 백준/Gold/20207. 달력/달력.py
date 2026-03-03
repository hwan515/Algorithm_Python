T = int(input())
N = [0] * 367
for i in range(T):
    start, end = map(int, input().split())
    for j in range(start, end + 1):
        N[j] += 1

total_area = 0
width = 0
height = 0
# 날짜 별로 돌면서 연속된 가장 긴 날짜 체크
for k in range(1, 367):
    # 일정이 있으면
    if N[k] != 0:
        width += 1
        height = max(height, N[k])
    # 일정이 끊기면
    else:
        area = width * height
        total_area += area
        width = 0
        height = 0

print(total_area)