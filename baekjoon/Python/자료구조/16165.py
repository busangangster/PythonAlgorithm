import sys
input = sys.stdin.readline
n,m = map(int,input().split())
group = []
for _ in range(n):
  team = input().strip()
  cnt = int(input())
  members = [input().strip() for _ in range(cnt)]
  members.sort()
  group.append([team,members])

for _ in range(m):
  s = input().strip()
  flag = int(input())
  if flag == 0:
    for x in group:
      if s == x[0]:
        for i in x[1]:
          print(i)
  else:
    for x in group:
      if s in x[1]:
        print(x[0])