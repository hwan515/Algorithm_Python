#백준 2562
def find_max_and_index(numbers):
    max_num = max(numbers)
    index = lambda x: numbers.index(x) + 1
    print(max_num)
    print(index(max_num))

numbers = [int(input()) for _ in range(9)]
find_max_and_index(numbers)