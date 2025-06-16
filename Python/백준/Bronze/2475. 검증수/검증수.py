def function(A, B, C, D, E):
    return (A**2 + B**2 + C**2 + D**2 + E**2) % 10

A, B, C, D, E = map(int, input().split())
print(function(A, B, C, D, E))
