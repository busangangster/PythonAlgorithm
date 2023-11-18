t = int(input())
for t_case in range(1,t+1):
  n,m,k = map(int,input().split())
  p = list(map(int,input().split()))
  p.sort()
  time = m
  bread = k

  while p:
    if p[0] <= time:
      if bread == 0:
        print('#{} Impossible'.format(t_case))
        break
      else:
        p.pop(0)
        bread -= 1
    time += m
    bread += k
    
  else: 
    print('#{} Possible'.format(t_case))