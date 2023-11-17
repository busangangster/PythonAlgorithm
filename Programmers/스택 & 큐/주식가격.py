
from collections import deque
def solution(prices):
    answer = []
    dq = deque(prices)
    while dq:
        sec = 0
        cur = dq.popleft()
        for x in dq:
            sec += 1 # 3 다음에 2가 오더라도 1초 뒤에 가격이 떨어지기 때문에
                     # 반복문을 돌면서부터 sec에  +1씩 해줘도 됨
            if cur > x:
                break
        answer.append(sec)
            
    return answer

