T = int(input())
answer = 0

def solve(text):
    visited = set()
    before = None
    for c in text:
        # 이미 앞에 있던 문자
        if c in visited:
            if before == c:
                before = c
                continue
            else:
                return False
        else:
            visited.add(c)
            before = c
    return True

for _ in range(T):
    text = input()
    if solve(text):
        answer += 1

print(answer)