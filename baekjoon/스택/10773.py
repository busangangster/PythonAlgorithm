import sys
k = int(sys.stdin.readline())
stack = []

for i in range(k):
  a = int(sys.stdin.readline())
  if a == 0:
    stack.pop()
  else:
    stack.append(a)

print(sum(stack))
