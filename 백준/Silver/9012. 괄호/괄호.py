T = int(input())
for _ in range(T):
    arr = list(map(str, input()))
    stack = []

    result = "YES"
    while arr:
        tmp = arr.pop(0)

        if not stack:
            if tmp == '(':
                stack.append(tmp)
            elif tmp == ')':
                result = "NO"
                break
        elif stack:
            if tmp == '(':
                stack.append(tmp)
            elif tmp == ')':
                stack.pop()
    if stack:
        result = "NO"
    print(result)