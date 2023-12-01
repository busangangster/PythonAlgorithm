t = int(input())
for tc in range(1,t+1):
  n = int(input())
  stack = []
  cnt = 0
  for _ in range(n):
    stack.append(int(input()))
  
  avg = sum(stack)//len(stack)
  for x in stack:
    if x < avg:
      cnt += avg - x

  print('#{} {}'.format(tc,cnt))
