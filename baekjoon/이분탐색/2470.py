# 이분검색이라고 해서 mid 다 mid 찾는건 아님
# 투포인터 생각. 

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
a.sort()

lt = 0
rt = n-1
answer = 21470000000

while lt < rt:
  mid = a[lt] + a[rt]
  if abs(mid) < answer:
    answer = abs(mid)
    ans = a[lt], a[rt]
  if mid == 0:
    break
  if mid > 0:
    rt -= 1
  else:
    lt += 1

for x in sorted(ans):
  print(x,end=' ')
  
