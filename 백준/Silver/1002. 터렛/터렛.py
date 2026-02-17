T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 거리의 제곱 계산
    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    add_r_sq = (r1 + r2) ** 2
    sub_r_sq = (r1 - r2) ** 2

    # 3. 조건 분기
    if dist == 0:  # 중심이 같을 때
        if r1 == r2:
            print(-1)  # 무한대
        else:
            print(0)  # 동심원 (반지름 다름)

    else:  # 중심이 다를 때
        if dist > add_r_sq:
            print(0)  # 두 원이 멀리 떨어져 안 만남
        elif dist < sub_r_sq:
            print(0)  # 한 원이 다른 원 안에 있어 안 만남
        elif dist == add_r_sq:
            print(1)  # 외접 (밖에서 한 점)
        elif dist == sub_r_sq:
            print(1)  # 내접 (안에서 한 점)
        else:
            print(2)  # 그 외에는 두 점