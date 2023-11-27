def pow(x,c):
  if c == 1:
    return x
  return x * pow(x,c-1)

for i in range(1,11):
  t = int(input())
  n,m = map(int,input().split())
  print('#{} {}'.format(i,pow(n,m)))