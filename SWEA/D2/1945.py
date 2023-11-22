t = int(input())
for t_case in range(1,t+1):
  n = int(input())
  ans = []
  i = 2
  while i <= n:
    if n % i == 0:
      ans.append(i)
      n = n // i
    else:
      i += 1
  print('#{}'.format(t_case),end= ' ')
  print(ans.count(2),ans.count(3),ans.count(5),ans.count(7),ans.count(11))