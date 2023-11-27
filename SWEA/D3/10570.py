t = int(input())
for t_case in range(1,t+1):
  a,b = map(int,input().split())
  cnt = 0
  for i in range(a,b+1):
    aa = str(i)
    k = i**0.5
    if k == int(k):
      if aa == aa[::-1] and str(int(k)) == str(int(k))[::-1]:
        cnt += 1
  
  print('#{} {}'.format(t_case,cnt))