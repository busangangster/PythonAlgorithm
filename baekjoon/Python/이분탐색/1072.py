

import sys,math as m
input = sys.stdin.readline
x,y = map(int,input().split())

lt = 1
rt = x
ans = 2147000000
#k = m.trunc((y/x)*100) => 파이썬 부동소수점 오차 
k = (y*100)//x

if k >= 99:
  print(-1)
else:
  while lt <= rt:
    mid = (lt+rt) // 2
    t = m.trunc((y+mid)*100/(x+mid))
    if t > k:
      ans = mid
      rt = mid - 1
    else:
      lt = mid + 1
  print(ans)

  


  