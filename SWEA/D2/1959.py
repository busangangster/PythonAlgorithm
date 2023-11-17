t = int(input())
for t_case in range(1,t+1):
  n,m = map(int,input().split())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))
  result = -int(1e9)
  if len(a) < len(b):
    for i in range(max(m,n)-min(m,n)+1):
      k = 0
      for j in range(len(a)):
        k += a[j] * b[j+i]
      result = max(result,k)
    print('#{} {}'.format(t_case,result))

  else:
    for i in range(max(m,n)-min(m,n)+1):
      k = 0
      for j in range(len(b)):
        k += b[j] * a[j+i]
      result = max(result,k)
    print('#{} {}'.format(t_case,result))