import sys
input = sys.stdin.readline

n,k = map(int,input().split())
a = list(map(int,input().split(',')))
cnt = n-1

for _ in range(k):
  for i in range(cnt):
    a[i] = a[i+1] - a[i]
  a.pop()
  cnt -= 1

for i in range(len(a)):
  if i == len(a) - 1:
    print(a[i])
  else:
    print(a[i],end=',')