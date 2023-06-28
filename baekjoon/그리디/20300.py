import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
a.sort()
q = deque(a)
ans = []

if n % 2 == 0: # 짝수
  for _ in range(n//2):
    ans.append(q.popleft() + q.pop())


else:
  ans.append(q.pop())
  for _ in range(n//2): # 홀수
    ans.append(q.popleft() + q.pop())
    
print(max(ans))