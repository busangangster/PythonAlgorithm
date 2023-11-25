import sys
input = sys.stdin.readline

a,b = map(int,input().split())
ans = 0
t = []

for i in str(a):
  t.append(int(i))

for j in str(b):
  ans += sum(t) * int(j)

print(ans)