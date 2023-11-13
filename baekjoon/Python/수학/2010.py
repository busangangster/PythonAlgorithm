import sys
input = sys.stdin.readline

n = int(input())
m = []
ans = 0
for _ in range(n):
  m.append(int(input()))

m.sort()
if max(m) == 1:
  print(1)
else:
  ans += sum(m[:-1])
  ans += m[-1] - (n-1)
  print(ans)