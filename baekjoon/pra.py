# import sys
# input = sys.stdin.readline

from collections import deque

t = int(input())

for i in range(t):
  n = int(input())
  a = list(map(int,input().split()))
  a = deque(a)
  cnt = 0
  price = 0
  ans = 0

  while a:
    t = max(a)
    if a[0] < max(a):
      price += a[0]
      cnt += 1
    elif a[0] == max(a):
      ans += t*cnt - price
      cnt = 0
      price = 0
    a.popleft()

  print('#',i+1,sep ='',end=' ')
  print(ans)



    
