import sys
input = sys.stdin.readline

n = int(input())
lt = 0
rt = n 

while lt <= rt:
  mid = (lt+rt) // 2
  if mid**2 == n:
    print(mid)
    break
  elif mid**2 > n:
    rt = mid - 1
  else:
    lt = mid + 1 
