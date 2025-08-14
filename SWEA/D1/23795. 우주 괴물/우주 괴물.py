T = int(input())
for test_case in range(1, 1+T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 외계인 찾기
    start_i = 0
    start_j = 0
    zero_cnt = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                start_i = i
                start_j = j
            if matrix[i][j] == 0:
                zero_cnt += 1

    dangerous_cnt = 0
    # 위로 가면 서 0의 갯수 탐색
    k = 1
    while start_i + k < N and matrix[start_i + k][start_j] == 0:
        dangerous_cnt += 1
        k += 1
    # 아래로 가면서 0의 갯수 탐색
    k = 1
    while 0 <= start_i - k and matrix[start_i - k][start_j] == 0:
        dangerous_cnt += 1
        k += 1
    # 오른쪽으로 가면서 탐색
    k = 1
    while start_j + k < N and matrix[start_i][start_j + k] == 0:
        dangerous_cnt += 1
        k += 1
    # 왼쪽으로 가면서 탐색
    k = 1
    while 0 <= start_j - k and matrix[start_i][start_j - k] == 0:
        dangerous_cnt += 1
        k += 1

    safety_zone = zero_cnt - dangerous_cnt

    print(f'#{test_case} {safety_zone}')