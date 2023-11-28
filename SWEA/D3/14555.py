t = int(input())
for tc in range(1,t+1):
  s = input()
  stack = []
  cnt = 0
  for x in s:
    if x == '(':
      stack.append(x)
    elif x == ')':
      if stack[-1] == '(' or stack[-1] == '|':
        cnt += 1
        stack.pop()
    elif x == '|':
      if stack and stack[-1] == '(':
        cnt += 1
        stack.pop()
      else:
        stack.append(x)

  print('#{} {}'.format(tc,cnt))