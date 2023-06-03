

import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
k = ['A','A']
t = ['B','B']

for _ in range(n):
  stack = []
  a = list(input().strip())

  for x in a:
    stack.append(x)
    if stack[-2:] == k or stack[-2:] == t:
      for _ in range(2):
        stack.pop()

  if not stack:
    cnt += 1

print(cnt)



