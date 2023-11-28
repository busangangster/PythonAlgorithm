t = int(input())
for tc in range(1,t+1):
  n = int(input())
  ans = 0
  for _ in range(n):
    a = list(input().split())
    ans += float(a[0]) * int(a[1])
  print('#{} {}'.format(tc,ans))