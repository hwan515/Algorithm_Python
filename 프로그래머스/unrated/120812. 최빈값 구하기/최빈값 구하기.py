from collections import Counter

def solution(array):
    answer = 0
    arr = Counter(array)
    count = 0
    
    max_value = max(arr.values())
    
    for key in arr:
        if arr[key] == max_value:
            count += 1 
            answer = key
    if count > 1:
        return -1
    
    return answer