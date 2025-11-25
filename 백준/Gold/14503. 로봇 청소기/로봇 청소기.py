N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 0은 청소되지 않은 칸(처음 모든 빈칸은 청소 X), 1은 벽을 의미
# - 현재 칸이 청소가 안되어 있다면 청소한다.
# - 주변 4칸 모두 깨끗한 경우,
#       바라보는 방향을 유지한 채 한 칸 후진하고 1번으로 돌아간다.
#       만약 뒤쪽이 벽이라면 작동을 멈춘다.
# - 주변 4칸 중 청소되지 않은 칸이 있는 경우,
#       반시계 방향으로 90도 회전한다.
#       바라보는 방향을 기준으로 앞쪽이 청소되지 않은 칸이라면 앞으로 한 칸 이동한다.
#       1번으로 돌아간다.

clean = [[0] * M for _ in range(N)]

def solve(r, c, d):
    global is_active
    global cnt

    if room[r][c] == 0 and clean[r][c] == 0:
        clean[r][c] = 1
        cnt += 1

    dirty = False
    for k in range(4):
        nr = r + dy[k]
        nc = c + dx[k]
        if 0 <= nr < N and 0 <= nc < M:
            if room[nr][nc] == 0 and clean[nr][nc] == 0:
                dirty = True
                break

    if dirty:
        # 청소할 곳이 있는 경우 (반시계 회전 -> 앞이 청소 안됐으면 전진)
        nd = d
        for _ in range(4):  # 최대 4번 회전 시도
            nd = (nd - 1 + 4) % 4  # 반시계 회전
            nr = r + dy[nd]
            nc = c + dx[nd]

            if 0 <= nr < N and 0 <= nc < M:
                if room[nr][nc] == 0 and clean[nr][nc] == 0:
                    solve(nr, nc, nd)  # 전진
                    return  # 전진했으면 현재 함수 종료
    else:
        # 청소할 곳이 없는 경우 (후진)
        # 바라보는 방향 유지한 채 뒤로
        back_d = (d + 2) % 4
        br = r + dy[back_d]
        bc = c + dx[back_d]

        if 0 <= br < N and 0 <= bc < M:
            if room[br][bc] == 1:  # 뒤가 벽이면
                return  # 작동 중지
            else:
                solve(br, bc, d)  # 방향 유지한 채 후진

cnt = 0

solve(r, c, d)

print(cnt)