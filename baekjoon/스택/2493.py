import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
ans = [0] * n
stack = []

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1] + 1
    stack.append(i)

print(*ans)



