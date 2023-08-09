import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
a.sort()

ans = 1

for i in a:
  if ans < i:
    break
  else:
    ans += i

print(ans)


