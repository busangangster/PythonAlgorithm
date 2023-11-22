t = int(input())
month = [0,31,59,90,120,151,181,212,243,273,304,334,365]

for t_case in range(1,t+1):
  a,b,c,d = map(int,input().split())
  ans = (month[c-1]+d) - (month[a-1]+ b) + 1
  print('#{} {}'.format(t_case,ans))