t = int(input())
for t_case in range(1,t+1):
  n = int(input())
  k = "1"+"/"+str(n)
  ans = []
  for _ in range(n):
    ans.append(k)

  print('#{}'.format(t_case),end=' ')
  print(*ans)