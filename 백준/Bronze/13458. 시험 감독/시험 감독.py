N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = N

for students in A:
    remaining = students - B
    
    if remaining > 0:
        if remaining % C == 0:
            answer += remaining // C
        else:
            answer += remaining // C + 1

print(answer)