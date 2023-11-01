import sys
input = sys.stdin.readline

n,x = map(int,input().split())
a = list(map(int,input().split()))

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

if max_v == 0:
  print('SAD')
else:
  print(max_v)
  print(cnt)