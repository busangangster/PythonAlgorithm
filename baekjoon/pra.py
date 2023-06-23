import sys
input = sys.stdin.readline

n,m = map(int,input().split())
j = int(input())
cnt = 0
cur = 1

for _ in range(j):
  a = int(input())

  if cur <= a and cur + (m-1) >= a:
    pass
  elif cur > a:
    cnt += abs(a-cur)
    cur = a
  else:
    cnt += a - (m-1) - cur
    cur = a - (m-1)


print(cnt)

