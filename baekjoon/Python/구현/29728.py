import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [True for _ in range(n+1)] # 다 소수로 초기화
flag = True
ans = deque('B') # n이 1인경우에는 소수가 아니기 때문에 미리 넣어두고 시작
b = 1
s = 0

for i in range(2,int(n**0.5)+1): # 소수 찾아내기, 에라토스테네스 체
  if arr[i] == True:
    j = 2
    while i * j <= n:
      arr[i*j] = False # 해당 수의 배수는 전부 소수가 아님 
      j += 1

for i in range(2,n+1): # 2부터 시작
  if arr[i]: # 소수인 경우 
    if flag == True:
      if ans[-1] == 'B':
        ans.pop()
        for _ in range(2):
          ans.append('S')
      else:
        ans.append('S')
        flag = False
    else:
      if ans[0] == 'B':
        ans.popleft()
        for _ in range(2):
          ans.appendleft('S')
      else:
        ans.appendleft('S')
        flag = True
  else: # 소수 아닐 때
    if flag == True:
      ans.append('B')
    else:
      ans.appendleft('B')

print(ans.count('B'),ans.count('S'))