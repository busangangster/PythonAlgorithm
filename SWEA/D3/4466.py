t = int(input())
for tc in range(1,t+1):
  n,k = map(int,input().split())
  a = sorted(list(map(int,input().split())),reverse=True)
  ans = 0
  for i in range(k):
    ans += a[i]
  print('#{} {}'.format(tc, ans))