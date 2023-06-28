import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
a.sort()
q = deque(a) # 큐를 사용해서 앞의 요소와 뒤의 요소를 추출
ans = []

if n % 2 == 0: # 짝수
  for _ in range(n//2):
    ans.append(q.popleft() + q.pop())

else: # 홀수
  ans.append(q.pop()) # 맨 끝 요소 제거해준 뒤 반복문 진행 
  for _ in range(n//2): 
    ans.append(q.popleft() + q.pop())
    
# min값이 아닌 max값을 출력해야 하는 이유는 근손실의 합인 M을 넘지 않아야 하기 때문 !
print(max(ans))  


