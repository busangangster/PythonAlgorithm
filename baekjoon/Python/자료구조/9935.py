

import sys
input = sys.stdin.readline

a = list(input().strip())
b = list(input().strip())
stack  = []

for i in a:
  stack.append(i)
  if stack[-len(b):] == b:
    for _ in range(len(b)):
      stack.pop()

if stack:
  print(''.join(stack))
else:
  print('FRULA')

  