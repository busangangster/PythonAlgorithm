t = int(input())
for tc in range(1,t+1):
  n,m = map(int,input().split())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))
  ans = -2147000000
  if len(b) >= len(a):
    for i in range(len(b)-len(a)+1):
      tmp = 0
      for j in range(len(a)):
        tmp += a[j]*b[i+j]
      ans = max(tmp,ans)
  else:
    for i in range(len(a)-len(b)+1):
      tmp = 0
      for j in range(len(b)):
        tmp += b[j]*a[i+j]
      ans = max(tmp,ans)

  print('#{} {}'.format(tc, ans))