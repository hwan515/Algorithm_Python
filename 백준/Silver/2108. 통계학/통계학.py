import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

# 1. 평균
mean = round(sum(nums) / n)

# 2. 중앙값
nums.sort()
median = nums[n // 2]

# 3. 최빈값
counter = Counter(nums)
most_common = counter.most_common()

if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    mode = most_common[1][0]
else:
    mode = most_common[0][0]

# 4. 범위
range_val = nums[-1] - nums[0]

# 출력
print(mean)
print(median)
print(mode)
print(range_val)