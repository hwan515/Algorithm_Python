from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    arr_input = input().rstrip()

    dq = deque()
    if n > 0:
        dq = deque(arr_input[1:-1].split(','))

    is_reversed = False
    is_error = False


    for cmd in p:
        if cmd == 'R':
            is_reversed = not is_reversed
        elif cmd == 'D':
            if not dq:
                print('error')
                is_error = True
                break

            if is_reversed:
                dq.pop()
            else :
                dq.popleft()

    if not is_error:
        if is_reversed:
            dq.reverse()

        print('[' + ','.join(dq) + ']')