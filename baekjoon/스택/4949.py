while True:
  n = input()
  stack = []
  if n == '.':
    break
  else:
    for x in n:
      if x == '(' or x == '[':
        stack.append(x)
      elif x == ')':
        if stack and stack[-1] == '(':
          stack.pop()
        else:
          stack.append(x)
      elif x == ']':
        if stack and stack[-1] == '[':
          stack.pop()
        else:
          stack.append(x)

  if not stack: # 스택이 비어있으면 yes. 짝이 맞음
    print('yes')
  else:
    print('no')
