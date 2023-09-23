import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  max_v = n
  while n != 1:
    if n % 2 == 0:
      n = n // 2
    else:
      n = (n*3)+1
    if n > max_v:
      max_v = n

  print(max_v)