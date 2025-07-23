N = int(input())
size_cnt = list(map(int, input().split()))
T, P = map(int, input().split())

# 티셔츠 묶음 수 계산
total = 0
for cnt in size_cnt:
    total += (cnt + T - 1) // T  # 올림 계산

print(total)

# 펜 묶음 수 계산
a = N // P  # 최대 몇 묶음
b = N % P   # 남은 개수

print(a, b)
