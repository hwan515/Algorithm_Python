def solution(a, b):
    i = int(str(a) + str(b))
    j = int(str(b) + str(a))
    
    if i >= j:
        return i
    elif j > i:
        return j
    
