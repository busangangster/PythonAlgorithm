t = int(input())

for t_case in range(1,t+1):
  a,b,c,d = map(int,input().split())
  s = a + c
  bun = b + d
  if bun >= 60:
    s += bun // 60
    bun = bun % 60
  if s > 12:
    if s % 12 == 0:
      s = 12
    else:
      s = s % 12

  print('#{} {} {}'.format(t_case,s,bun))