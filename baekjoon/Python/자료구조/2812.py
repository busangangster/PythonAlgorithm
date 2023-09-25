

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
a  = input().strip()
stack = []

for x in a:
    while stack and k > 0:
        if stack[-1] < x:
            stack.pop()
            k -= 1
        else:
            break
    stack.append(x)

if k >0 :
    for _ in range(k):
        stack.pop()

print(''.join(stack))

