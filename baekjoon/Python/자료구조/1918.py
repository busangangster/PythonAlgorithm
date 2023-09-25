

import sys
input = sys.stdin.readline

n = input()
ans = ''
stack = []

for x in n:
  if x.isalpha():
    ans += x
  else:
    if x == '(':
      stack.append(x)
    elif x == '+' or x == '-':
      while stack and stack[-1] != '(':
        ans += stack.pop()
      stack.append(x)
    elif x == '*' or x == '/':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        ans += stack.pop()
      stack.append(x)
    elif x == ')':
      while stack and stack[-1] != '(':
        ans += stack.pop()
      stack.pop()

while stack:
  ans += stack.pop()

print(ans)



