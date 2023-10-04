import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
a = deque(a)
stack = []
num = 1

while a:
  if a[0] == num:
    a.popleft()
    num += 1
  else:
    stack.append(a.popleft())

  while stack:
    if stack[-1] == num:
      stack.pop()
      num += 1
    else:
      break

if stack:
  print('Sad')
else:
  print('Nice')
