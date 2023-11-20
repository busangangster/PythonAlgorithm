t = int(input())

# def GCD(x,y):
#   while y != 0:
#     s = x % 
#     x = y
#     y = s

#   return x

for t_case in range(1,t+1):
  a,b = map(int,input().split())
  ans = 0
  if a == b:
    print('#{} {}'.format(t_case,a))
  else:
    print('#{} {}'.format(t_case,1))