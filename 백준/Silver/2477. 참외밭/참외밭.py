K = int(input())
# 동:1, 서:2, 남:3, 북:4
dists = []
max_row = [-1, -1]
max_col = [-1, -1]

for i in range(6):
    d, dist = map(int, input().split())
    dists.append(dist)
    if d == 1 or d == 2:
        if max_row[1] < dist:
            max_row[1] = dist
            max_row[0] = i
    else:
        if max_col[1] < dist:
            max_col[1] = dist
            max_col[0] = i

# 가장 큰 사각형에서 빼야하는 빈 사각형 빼기
# 가장 긴 가로변에서 +3 idx를 하면 빼야하는 세로변
# 가장 긴 세로변에서 +3 idx를 하면 빼야하는 가로변

d_row = (max_col[0] + 3) % 6
d_col = (max_row[0] + 3) % 6


result = ((max_row[1] * max_col[1]) - (dists[d_row] * dists[d_col])) * K
print(result)