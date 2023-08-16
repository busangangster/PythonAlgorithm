import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque()
stack = []

for _ in range(n):
  a = list(map(str,input().split()))

  if a[0] == '1':
    stack.append([a[1],1])
    arr.append(a[1])
  elif a[0] == '2':
    stack.append([a[1],2])
    arr.appendleft(a[1])
  else:
    if stack:
      if stack[-1][1] == 1:
        arr.pop()
        stack.pop()
      elif stack[-1][1] == 2:
        arr.popleft()
        stack.pop()

if arr:
  print(''.join(arr))
else:
  print(0)
