import sys
from collections import deque
input = sys.stdin.readline

n,s = map(int,input().split())
arr = list(map(int,input().split()))
lt = 0
rt = 0
tmp = 2147000000
ans = 0

while True: 
  if ans >= s:
    tmp = min(tmp,rt - lt)
    ans -= arr[lt]
    lt += 1
  elif rt == n:
    break
  else:
    ans += arr[rt]
    rt += 1

if tmp == 2147000000:
  print(0)
else:
  print(tmp)