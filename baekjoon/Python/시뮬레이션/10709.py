import sys
input = sys.stdin.readline

h,w = map(int,input().split())
a = []

for _ in range(h):
  a.append(list(input().strip()))

check = [[0] * w  for _ in range(h)]

for i in range(h):
  cnt = 0
  cloud = False
  for j in range(w):
    if not cloud and a[i][j] == '.':
      check[i][j] = -1

    elif a[i][j] == 'c':
      cloud = True
      check[i][j] = 0
      cnt = 1

    elif cloud and a[i][j] == '.':
      check[i][j] = cnt
      cnt += 1

for x in check:
  print(*x)