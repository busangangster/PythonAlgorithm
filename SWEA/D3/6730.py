t = int(input())
for t_case in range(1,t+1):
  n = int(input())
  a = list(map(int,input().split()))
  up = 0 
  down = 0
  for i in range(n-1):
    if a[i] < a[i+1]:
      up = max(up,a[i+1]-a[i])
    elif a[i] > a[i+1]:
      down = max(down,a[i]-a[i+1])
  print('#{} {} {}'.format(t_case,up,down))