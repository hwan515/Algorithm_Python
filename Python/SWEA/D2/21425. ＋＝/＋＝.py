T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A, B, N = map(int, input().split())
    
    count = 0
    
    if A > B:
        A, B = B, A
    
    while N >= B:
        A, B = B, A + B
        count += 1
        
    print(count)