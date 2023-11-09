import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  exp = n*(n+1)//2
  lt,rt = 1,10**9
  while lt <= rt:
    mid = (lt+rt)// 2
    k = mid*(mid+1)
    if k <= exp:
      lt = mid + 1
    else:
      rt = mid - 1
  print(lt)