t = int(input())
for t_case in range(1,t+1):
  a = list(map(int,input().split()))
  a.sort()
  a.pop(0)
  a.pop()
  print('#{} {}'.format(t_case,round(sum(a)/len(a))))