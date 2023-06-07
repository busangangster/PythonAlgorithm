import sys
input = sys.stdin.readline

n = int(input())
cents = [25,10,5,1]


for _ in range(n):
  k = int(input())
  ans = []
  for x in cents:
    ans.append(k//x)
    k = k%x

  print(*ans)