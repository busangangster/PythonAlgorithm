import sys
input = sys.stdin.readline

n = int(input())
s = list(input().strip())
cnt = 0 
stack = []
g = []

for i in s:
  if stack:
    if stack[-1] == '(' and i == ')':
      stack.pop()
    elif stack[-1] == ')' and i == '(':
      stack.pop()
    else:
      stack.append(i)
  else:
    stack.append(i)

  g.append(len(stack))

if stack:
  print(-1)
else:
  print(max(g))