N = int(input())
numbers = map(int, input().strip())

result = 0
for number in numbers:
    result += number
print(result)