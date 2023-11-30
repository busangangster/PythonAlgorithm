t = int(input())
for tc in range(1,t+1):
  n,a,b = map(int,input().split())
  ans1 = min(a,b)
  ans2 = a+b - n
  if ans2 <= 0:
    ans2 = 0
  print('#{} {} {}'.format(tc,ans1,ans2))