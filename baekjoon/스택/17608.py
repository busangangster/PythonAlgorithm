

import sys
input = sys.stdin.readline

n = int(input())
k = []
stack = []
for _ in range(n):
  k.append(int(input()))

for i in k:
  while stack and stack[-1] <= i:
    stack.pop()
  stack.append(i)

print(len(stack))





  