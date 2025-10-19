while True:
    text = input()
    if text == '.':
        break

    stack = []
    flag = True
    for c in text:
        if not flag:
            break
        if c == '(' or c == '[':
            stack.append(c)

        elif c == ')' or c == ']':
            if stack:
                tmp = stack.pop()
                if tmp == '(' and c == ')':
                    continue
                elif tmp == '[' and c == ']':
                    continue
                else:
                    flag = False
                    break
            else:
                flag = False
                break

    if stack:
        print('no')
    else:
        if not flag:
            print('no')
        else:
            print('yes')