x, y, w, h = map(int, input().split())

# 4개의 거리 중 최솟값을 계산하여 출력
print(min(x, y, w-x, h-y))