t = int(input())
for tc in range(1,t+1):
  a,b,c = map(int,input().split())
  t = min(a,b)
  k = max(a,b)
  ans = 0
  ans += c // t
  c = c % t
  ans += c // k

  print('#{} {}'.format(tc,ans))