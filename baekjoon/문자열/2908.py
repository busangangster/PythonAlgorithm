import sys

a,b = sys.stdin.readline().split()
a = a[::-1]
b = b[::-1]

ans = []
ans.append(a)
ans.append(b)

print(max(ans))