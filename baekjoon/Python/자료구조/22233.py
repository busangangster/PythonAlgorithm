import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dic = {}
for _ in range(n):
  a = input().strip()
  dic[a] = 1

ans = n
for _ in range(m):
  a = list(input().strip().split(','))
  for x in a:
    if x in dic:
      dic[x] -= 1
      if dic[x] == 0:
        ans -= 1

  print(ans)