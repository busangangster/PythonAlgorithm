import sys
input = sys.stdin.readline

n = int(input())
arr = []
stack = []
ans = 0

for _ in range(n):
  arr.append(int(input()))


for i in arr:
  while stack and stack[-1] <= i:
    stack.pop()
  stack.append(i)
  ans += len(stack)- 1

print(ans)