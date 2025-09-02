N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]
min_count = 64  # 8x8 체스판의 최대 수정 횟수는 64

# 1. 8x8 체스판의 시작점을 모두 순회
for i in range(N-7):
    for j in range(M-7):

        count_W = 0
        count_B = 0

        # 체스판 조사
        for si in range(i, i + 8):
            for sj in range(j, j + 8):

                # 홀짝으로 올바른 색깔 판단
                if (si + sj) % 2 == 0:
                    if board[si][sj] == 'W': # B로 시작하는 패턴
                        count_B += 1  # B로 바꿔야함
                    if board[si][sj] == 'B': # W로 시작하는 패턴
                        count_W += 1  # W로 바꿔야함
                else:
                    if board[si][sj] == 'B': # B로 시작하는 패턴
                        count_B += 1
                    if board[si][sj] == 'W': # W로 시작하는 패턴
                        count_W += 1

        current_min = min(count_W, count_B)
        if current_min < min_count:
            min_count = current_min

print(min_count)