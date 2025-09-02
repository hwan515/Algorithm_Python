while True: # 무한 루프
    num = int(input())
    if num == 0:
        break
    
    str_num = str(num)
    num_list = list(map(int, str_num))
    rev_num_list = num_list[::-1]
    if num_list == rev_num_list:
        print("yes")
    else:
        print("no")