import sys

# 1. 숫자 개수를 셀 리스트를 초기화합니다. (숫자는 1~10000이므로 크기는 10001)
counts = [0] * 10001

# 2. N을 입력받고, N번 반복하며 숫자의 개수를 셉니다.
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    counts[num] += 1

# 3. 개수 리스트를 순회하며 결과를 출력합니다.
for i in range(1, 10001):
    if counts[i] != 0:
        # 해당 숫자를 개수만큼 반복해서 출력
        for _ in range(counts[i]):
            print(i)