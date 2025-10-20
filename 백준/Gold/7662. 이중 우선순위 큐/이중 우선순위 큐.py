import sys
import heapq

# 입력을 빠르게 받기 위함
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 최소 힙, 최대 힙
    min_heap = []
    max_heap = []
    # 각 숫자의 개수를 저장하여 동기화에 사용
    # key: 숫자, value: 해당 숫자의 개수
    num_counts = {}

    K = int(input())
    for _ in range(K):
        op, num_str = input().split()
        num = int(num_str)

        if op == 'I':
            # 삽입 연산
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)  # 최대 힙은 부호를 바꿔서 저장
            # 숫자의 개수 업데이트
            num_counts[num] = num_counts.get(num, 0) + 1

        elif op == 'D':
            if num == 1:  # 최댓값 삭제
                # 1. max_heap이 비어있으면 무시
                # 2. top이 유효하지 않으면(이미 min_heap에서 삭제된 값이면) 제거
                while max_heap and num_counts[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)

                # 3. 유효한 원소가 있으면 삭제하고 개수 차감
                if max_heap:
                    deleted_num = -heapq.heappop(max_heap)
                    num_counts[deleted_num] -= 1
            else:  # 최솟값 삭제
                # 1. min_heap이 비어있으면 무시
                # 2. top이 유효하지 않으면(이미 max_heap에서 삭제된 값이면) 제거
                while min_heap and num_counts[min_heap[0]] == 0:
                    heapq.heappop(min_heap)

                # 3. 유효한 원소가 있으면 삭제하고 개수 차감
                if min_heap:
                    deleted_num = heapq.heappop(min_heap)
                    num_counts[deleted_num] -= 1

    # 최종 결과를 출력하기 전, 두 힙에 남아있는 유령 데이터들을 모두 정리
    while max_heap and num_counts[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    while min_heap and num_counts[min_heap[0]] == 0:
        heapq.heappop(min_heap)

    # 정리 후 힙이 비어있으면 EMPTY 출력
    if not min_heap:
        print("EMPTY")
    else:
        # 최대 힙의 top과 최소 힙의 top 출력
        max_val = -max_heap[0]
        min_val = min_heap[0]
        print(max_val, min_val)