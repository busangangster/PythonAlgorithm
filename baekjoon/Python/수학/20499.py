import sys
input = sys.stdin.readline

a = input().strip().split("/")
if (int(a[0]) + int(a[2])) < int(a[1]) or int(a[1]) == 0:
  print('hasu')
else:
  print('gosu')