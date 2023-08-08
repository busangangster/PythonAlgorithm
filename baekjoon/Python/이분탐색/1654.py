import sys
k,n = map(int,sys.stdin.readline().split())
a= []

for _ in range(k):
  tmp = int(input())
  a.append(tmp)

lt = 1
rt = max(a)
res = 0

def Count(x):
  cnt = 0
  for i in a:
    cnt += i//x
  return cnt


while lt <= rt:
  mid = (lt+rt) // 2
  if Count(mid) >= n:
    res = mid
    lt = mid +1
  else:
    rt = mid -1

print(res)