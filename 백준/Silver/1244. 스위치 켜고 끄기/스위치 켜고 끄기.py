N = int(input())
switches = list(map(int, input().split()))
M = int(input())
students = [list(map(int, input().split())) for _ in range(M)]

for student in students:
    if student[0] == 1: # 남자
        k = 1
        while student[1] * k <= N:
            switches[student[1] * k - 1] = 1 - switches[student[1] * k - 1]
            k += 1

    else: # 여자
        idx = student[1] - 1  # 인덱스 값으로 변경
        switches[idx] = 1 - switches[idx]
        k = 1
        while 0 <= idx - k and idx + k < N and switches[idx - k] == switches[idx + k]:
            switches[idx - k] = 1 - switches[idx - k]
            switches[idx + k] = 1 - switches[idx + k]
            k += 1

for i in range(0, N, 20):
    print(*switches[i:i + 20])