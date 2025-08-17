row, col = map(int, input().split())
N = int(input())

# 잘라야 하는 위치 입력 받고 추가
cut_row = []
cut_col = []
for _ in range(N):
    i, j = map(int, input().split())

    if i == 0:
        cut_row.append(j)
    else:
        cut_col.append(j)
cut_row.append(col)
cut_col.append(row)
cut_row.append(0)
cut_col.append(0)

cut_row.sort()
cut_col.sort()

max_row = cut_row[0]
for i in range(1, len(cut_row)):
    if max_row < cut_row[i] - cut_row[i - 1]:
        max_row = cut_row[i] - cut_row[i - 1]

max_col = cut_col[0]
for i in range(1, len(cut_col)):
    if max_col < cut_col[i] - cut_col[i - 1]:
        max_col = cut_col[i] - cut_col[i - 1]

print(max_row * max_col)
