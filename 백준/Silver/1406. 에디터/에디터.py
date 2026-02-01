text = input().strip()
M = int(input())

left = list(text)
right = []

for _ in range(M):
    cmd = input().split()

    if cmd[0] == 'L':
        # left -> right로 1개 이동
        if left:
            right.append(left.pop())
    elif cmd[0] == 'D':
        # right -> left로 1개 이동
        if right:
            left.append(right.pop())

    elif cmd[0] == 'B':
        # left에서 삭제
        if left:
            left.pop()
    else:  # 'P'
        # left에 문자 추가 (cmd[1])
        left.append(cmd[1])

print(''.join(left + right[::-1]))