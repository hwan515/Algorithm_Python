# 세로, 가로, 인벤
N, M, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 블록 제거는 2초, 블록 놓기는 1초

# 행렬에서 최대값 찾기
max_num = max(map(max, matrix))
min_num = min(map(min, matrix))

time = 21e8
height = 21e8
for num in range(min_num, max_num + 1):
    add_block = 0    # 블럭 놓기는 1초
    remove_block = 0 # 블럭 제거는 2초
    for i in range(N):
        for j in range(M):
            tmp = num - matrix[i][j]
            if tmp < 0:
                remove_block -= tmp
            else:
                add_block += tmp

    # 시간 계산
    tmp_time = -1
    if add_block <= B + remove_block:
        tmp_time = add_block + remove_block * 2
        if tmp_time < time:
            time = tmp_time
            height = num
        elif tmp_time == time:
            height = num

print(time, height)