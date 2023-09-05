import sys
input = sys.stdin.readline

a = list(input().strip())
stack = []
ans = 0
cnt = 0

for i in a:
  if i == '(' or '[':
    stack.append(i)
  else:
    if i == ')':
      while stack[-1] != '(':
        stack.pop()
    elif i == ']':
      while stack[-1] != '[':
        stack.pop()
      cnt += 1


