import sys
input = sys.stdin.readline

n = int(input())
a = list(input().strip())
plus = 0
ans = 0

for i in range(n):
  if a[i] == 'O':
    ans += i+1
    ans += plus
    plus += 1
  else:
    plus = 0
print(ans)