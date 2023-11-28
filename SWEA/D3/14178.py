t = int(input())
for tc in range(1,t+1):
  n,d = map(int,input().split())
  k = d*2 + 1
  ans = n/k 
  if ans > n // k:
    ans = n//k + 1
  else:
    ans = n//k
  print('#{} {}'.format(tc,ans))