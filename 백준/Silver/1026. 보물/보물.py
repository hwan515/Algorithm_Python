N = int(input())
A = sorted(map(int, input().split()))
B = sorted(sorted(map(int, input().split())), reverse=True)

answer = 0
for i in range(N):
    answer = answer + A[i] * B[i]
print(answer)