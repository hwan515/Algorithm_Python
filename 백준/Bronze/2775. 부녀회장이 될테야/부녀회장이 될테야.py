T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())

    matrix = [[0] * (N + 1) for _ in range(K + 1)]

    for j in range(1, N + 1):
        matrix[0][j] = j
    
    for i in range(1, K + 1):
        for j in range(1, N + 1):
            matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]

    print(matrix[K][N])