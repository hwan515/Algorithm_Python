S, P = map(int, input().split())
dna = input()
min_counts = list(map(int, input().split()))

dic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
arr = [0] * 4
result = 0


def is_valid():
    for i in range(4):
        if arr[i] < min_counts[i]:
            return False
    return True

for i in range(P):
    idx = dic[dna[i]]
    arr[idx] += 1

if is_valid():
    result += 1

for i in range(P, S):
    add_idx = dic[dna[i]]
    arr[add_idx] += 1

    remove_idx = dic[dna[i-P]]
    arr[remove_idx] -= 1

    if is_valid():
        result += 1

print(result)