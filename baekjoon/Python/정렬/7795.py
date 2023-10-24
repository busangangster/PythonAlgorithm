import sys
input = sys.stdin.readline

def binary(x):
  res = 0
  left = 0
  right = m - 1

  while left <= right:
    mid = (left + right) // 2

    if x > b[mid]:
      res = mid
      left = mid + 1
    else:
      right = mid - 1

  return res + 1

t = int(input())
for _ in range(t):
  n,m = map(int,input().split())
  a = sorted(list(map(int,input().split())))
  b = sorted(list(map(int,input().split())))
  cnt = 0
  for i in a:
    if i > b[0]:
      cnt += binary(i)
  print(cnt)