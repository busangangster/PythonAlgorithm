import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n,m = map(int,input().split())
  x = int(''.join(list(input().split())))
  y = int(''.join(list(input().split())))
  a = list(map(int,input().split()))
  a = a + a[:m-1]
  cnt = 0

  for i in range(n):
    check = int(''.join(map(str,a[i:i+m])))
    if x <= check <= y:
      cnt += 1
  print(cnt)


