import sys
input = sys.stdin.readline
a = ['a','e','i','o','u','A','E','I','O','U']
while True:
  cnt = 0
  s = input().strip()
  if s == '#':
    break
  for x in s:
    if x in a:
      cnt += 1
  print(cnt)

  