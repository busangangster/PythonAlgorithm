import sys
input = sys.stdin.readline

n = int(input())
cows = []
ans = 0

for _ in range(n):
  cows.append(list(map(int,input().split())))

cows.sort()

for i in cows:
  if ans < i[0]:
    ans = i[0] + i[1]
  else:
    ans += i[1]


print(ans)