import sys
input = sys.stdin.readline

a = list(input().strip())
n = 1
idx = 0

while True:
  for x in str(n):
    if x == a[idx]:
      idx += 1
      if idx >= len(a):
        print(n)
        sys.exit()
  n += 1