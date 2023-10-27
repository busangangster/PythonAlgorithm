import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

lt = 1
rt = k

while lt <= rt:
  tmp = 0
  mid = (lt + rt) // 2
  print(mid)

  for i in range(1,n+1):
    tmp += min(mid//i,n)

  if tmp >= k :
    ans = mid
    rt = mid - 1
  else:
    lt = mid + 1 

print(ans)
