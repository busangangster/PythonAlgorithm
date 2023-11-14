t = int(input())
for _ in range(t):
  n = int(input())
  g = 0
  gg = 0
  for _ in range(n):
    a,b = map(float,input().split())
    gg += a
    g += a*b
  print('{} {:.1f}'.format(int(gg),g/int(gg)))