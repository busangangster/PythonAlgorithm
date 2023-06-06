

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

ans = [-1] * n
stack = []
dict = {}

for x in a:
  if x in dict:
    dict[x] += 1
  else:
    dict[x] = 1

for i in range(len(a)):
  while stack and dict[a[stack[-1]]] < dict[a[i]]:
    ans[stack.pop()] = a[i]
  stack.append(i)

print(*ans)

