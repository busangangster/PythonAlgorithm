import sys
input = sys.stdin.readline

n,x = map(int,input().split())
a = list(map(int,input().split()))

if max(a) == 0:
  print('SAD')

else:
  cnt = 1
  window = sum(a[:x])
  max_v = window
  for i in range(x,n):
    window += a[i] - a[i-x]

    if max_v < window:
      max_v = window
      cnt = 1
    elif max_v == window:
      cnt += 1

  print(max_v)
  print(cnt)