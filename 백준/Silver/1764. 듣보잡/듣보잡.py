N, M = map(int, input().split())
hash_map = {}
result = []
for _ in range(N):
    name = input()
    hash_map[name] = True

for _ in range(M):
    name = input()
    if name in hash_map:  # 딕셔너리에 이름이 있는지 확인
        result.append(name)


result.sort()
print(len(result))
for name in result:
    print(name)