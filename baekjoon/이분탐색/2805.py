import sys
n,m = map(int,sys.stdin.readline().split())
a = list(map(int,input().split()))
res = 0

def Count(x):
  sum = 0
  for i in a:
    if i >= x:
      sum += i-x
  return sum 

lt = 1
rt = max(a)

while lt <= rt:
  mid = (lt+rt) // 2
  if Count(mid) < m:
    rt = mid - 1
  else:
    res = mid
    lt = mid + 1

print(res)