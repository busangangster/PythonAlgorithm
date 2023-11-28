
for tc in range(1,11):
  n,s = map(str,input().split())
  stack = []
  for x in s:
    if not stack:
      stack.append(x)
    else:
      if stack[-1] == x:
        stack.pop()
      else:
        stack.append(x)
  ans = ''.join(map(str,stack))
  print('#{} {}'.format(tc,ans))
