def is_hashing(text):
    hash_value = 0
    M = 1234567891
    R = 31
    for i in range(len(text)):
        hash_value += numbering_alpa(text[i]) * (R ** i)
    return hash_value % M
    
    
def numbering_alpa(alpa):
    result = ord(alpa) - ord('a') + 1
    return result

L = int(input())
text = input()

result = is_hashing(text)
print(result)