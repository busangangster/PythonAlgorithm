import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [True for _ in range(n+1)]
a = deque('B')
prime = []
s = 0
b = 1
flag = True
for i in range(2,int(n**0.5)+1):
  if arr[i] == True:
    j = 2
    while i*j <= n:
      arr[i*j] = False
      j += 1

for i in range(2,n+1):
  if arr[i]:
    if flag == True:
      if a[-1] == 'B':
        a.pop()
        b -= 1
        for _ in range(2):
          a.append('S')
        s += 2
      else:
        a.append('S')
        s += 1
        flag = False

    else:
      if a[0] == 'B':
        a.popleft()
        b -= 1
        for _ in range(2):
          a.appendleft('S')
        s += 2
      else:
        a.appendleft('S')
        s += 1
        flag = True

  else:
    if flag == 1:
      a.append('B')
    else:
      a.appendleft('B')
    b += 1
print(b,s)
