N = int(input())
n_arr = list(map(int, input().split()))
M = int(input())
m_arr = list(map(int, input().split()))

n_arr.sort()

for  i in m_arr:
    start = 0
    end = N-1

    found = 0

    while start <= end:
        mid = (start+end) // 2

        if n_arr[mid] > i:
            start = 0
            end = mid - 1

        elif n_arr[mid] < i:
            start = mid + 1

        elif n_arr[mid] == i:
            found = 1
            break

    print(found)