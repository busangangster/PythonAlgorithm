import sys
input = sys.stdin.readline

while True:
  a = input().strip()
  if a == 'END':
    break
  print(a[::-1])