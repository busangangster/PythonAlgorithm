import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
res = 0

lt = 0
rt = max(a) 

def Count(x):
  sum = 0
  for i in a:
    if i >= x:
      sum += x
    else:
      sum += i
  return sum

while lt <= rt:
  mid = (lt+rt) // 2
  if Count(mid) <= m:
    res = mid
    lt = mid + 1
  else:
    rt = mid - 1
    
print(res)