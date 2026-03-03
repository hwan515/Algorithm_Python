H, W = map(int, input().split())
heights = list(map(int, input().split()))

total = 0
for i in range(1, W - 1):
    # i번째 기준에서 왼쪽에서 가장 높은 기둥
    max_left = max(heights[:i + 1])

    # i번째 기준에서 오른쪽에서 가장 높은 기둥
    max_right = max(heights[i:W])

    # 두 높이중 가장 작은게 물이 찰 수 있는 높이
    max_height = min(max_left, max_right)
    
    total += max_height - heights[i]

print(total)