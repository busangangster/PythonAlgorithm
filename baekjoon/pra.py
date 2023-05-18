import sys
input = sys.stdin.readline

n = list(input().strip())
m = int(input())
stack = []

for _ in range(m):
  a = list(input().split())
  if a[0] == 'L':
    if n:
      stack.append(n.pop())
  elif a[0] == 'D':
    if stack:
      n.append(stack.pop())
  elif a[0] == 'B':
    if n:
      n.pop()
  elif a[0] == 'P':
    n.append(a[1])


n.extend(reversed(stack))

for x in n:
  print(x,end='')


