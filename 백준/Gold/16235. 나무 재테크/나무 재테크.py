from collections import deque
# k년
n, m, k = map(int, input().split())
nutrition = [list(map(int, input().split())) for _ in range(n)]

# x, y, z = (위치), 나이
trees = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = list(map(int, input().split()))
    x -= 1
    y -= 1
    trees[x][y].append(z)
# print(trees)


# n*n 크기 땅
# r,c는 1 시작
# 처음 양분은 모든 칸에 5
# m개의 나무 구매(1칸에 여러개 나무를 심을 수 있음)

# 봄
# - 나이만큼 양분을 먹고, 나이 +1 (1*1 크기에서만 양분 섭취 가능)
# - 한칸에 여러개 나무가 있다면 나이가 작은 순 부터 양분 섭취
# - 땅에 양분이 부족하여 자신의 나이만큼 못먹으면 나무 사망

# 여름
# - 봄에 죽은 나무가 양분으로 바뀜 (양분 = 죽은 나무 나이 // 2)

# 가을
# - 5의 배수여야만 번식, 인접 8칸에 나이 1인 나무 생김

# 겨울
# -  ground[r][c]에 양분 추가

ground = [[5] * n for _ in range(n)]
dead_tree = []

while True:
    if k == 0:
        break

    for season in range(4):
        # 봄
        if season == 0:
            tmp_tree = deque([])
            for i in range(n):
                for j in range(n):
                    # 해당 위치에 나무가 존재하면
                    if trees[i][j]:
                        # 작은 것부터 꺼내야함
                        tmp_tree = deque([])
                        while trees[i][j]:
                            tree = trees[i][j].popleft()
                            # 양분이 있으면 나이만큼 양분 빼고 나이 먹음
                            if ground[i][j] >= tree:
                                ground[i][j] -= tree
                                tree += 1
                                tmp_tree.append(tree)
                            else: # 양분이 나이보다 적으면
                                dead_tree.append([i, j, tree//2])
                        trees[i][j] = tmp_tree

        # 여름
        elif season == 1:
            while dead_tree:
                i, j, p = dead_tree.pop()
                ground[i][j] += p
        # 가을
        elif season == 2:
            for i in range(n):
                for j in range(n):
                    if trees[i][j]:
                        for tree in trees[i][j]:
                            if tree % 5 == 0:
                                if 0 <= i - 1 < n and 0 <= j - 1 < n:
                                    trees[i - 1][j - 1].appendleft(1)
                                if 0 <= i - 1 < n:
                                    trees[i - 1][j].appendleft(1)
                                if 0 <= j - 1 < n:
                                    trees[i][j - 1].appendleft(1)
                                if 0 <= i - 1 < n and 0 <= j + 1 < n:
                                    trees[i - 1][j + 1].appendleft(1)
                                if 0 <= i + 1 < n and 0 <= j - 1 < n:
                                    trees[i + 1][j - 1].appendleft(1)
                                if 0 <= i + 1 < n:
                                    trees[i + 1][j].appendleft(1)
                                if 0 <= j + 1 < n:
                                    trees[i][j + 1].appendleft(1)
                                if 0 <= i + 1 < n and 0 <= j + 1 < n:
                                    trees[i + 1][j + 1].appendleft(1)

        elif season == 3:
            for i in range(n):
                for j in range(n):
                    ground[i][j] += nutrition[i][j]

    k -= 1

total = 0
for ii in range(n):
    for jj in range(n):
        total += len(trees[ii][jj])

print(total)