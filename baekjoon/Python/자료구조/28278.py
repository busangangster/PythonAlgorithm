import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
  a = list(map(int,input().split()))

  if a[0] == 1:
    stack.append(a[1])
  elif a[0] == 2:
    if stack:
      print(stack.pop())
    else:
      print(-1)
  elif a[0] == 3:
    print(len(stack))
  elif a[0] == 4:
    if stack:
      print(0)
    else:
      print(1)
  else:
    if stack:
      print(stack[-1])
    else:
      print(-1)



