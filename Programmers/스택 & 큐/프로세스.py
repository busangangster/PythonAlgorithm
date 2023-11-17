from collections import deque
def solution(priorities, location):
    answer = 0
    # priorities 리스트를 (인덱스,값) 구조로 deque로 만들어줌 
    dq = list((idx,val) for idx, val in enumerate(priorities))
    dq = deque(dq)
    
    while dq:
        cur = dq.popleft()
        # 하나를 popleft()하고, 
        # 그 값의 우선순위보다 큰 우선순위인 값이 dq안에 존재하면 false로 다시 dq에 추가
        # 존재하지 않으면 true
        if any(cur[1] < x[1] for x in dq):
            dq.append(cur)
        else:
            answer += 1
            # 출력된 값의 idx가 location과 같으면 반복문 종료
            if cur[0] == location:    
                return answer