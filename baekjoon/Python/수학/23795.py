import sys
input = sys.stdin.readline
ans = 0
while True:
  a = int(input())
  if a == -1:
    break
  else:
    ans += a

print(ans)  