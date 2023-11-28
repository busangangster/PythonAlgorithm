t = int(input())
for tc in range(1,t+1):
  n,m = map(int,input().split())
  a = list(map(int,input().split()))
  ans = []
  for i in range(1,n+1):
    if i not in a:
      ans.append(i)
  print('#{}'.format(tc),end=' ')
  print(*ans)
