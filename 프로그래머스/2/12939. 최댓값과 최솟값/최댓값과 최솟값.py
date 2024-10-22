def solution(s):
    new_s = s.split()  # 문자열을 공백 기준으로 나눔
    l = len(new_s)  # 리스트의 길이를 구함
    
    ### new_s.sort()처음에는 이렇게 해서 사전순
    ### new_s.sort(key=int) 숫자로 정렬
    new_s.sort(key=int)  
    
    first = new_s[0]  # 첫 번째 값 (최소값)
    last = new_s[l-1]  # 마지막 값 (최대값)
    
    # first와 last를 사용하여 answer 계산
    answer = first + " " + last
    
    return answer  # 정답 반환
