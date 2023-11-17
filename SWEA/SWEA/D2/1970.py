t = int(input())
for t_case in range(1,t+1):
  n = int(input())
  ans = []
  money = [50000,10000,5000,1000,500,100,50,10]

  for x in money:
    ans.append(n//x)
    n = n % x
  print('#{}'.format(t_case)) 
  print(*ans)