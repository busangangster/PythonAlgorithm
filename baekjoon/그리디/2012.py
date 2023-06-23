import sys
input = sys.stdin.readline

n = int(input())
ex = []
ans = 0

for _ in range(n):
  ex.append(int(input()))

ex.sort()


for i in range(1,n+1):
  ans += abs(ex[i-1] - i)

print(ans)
