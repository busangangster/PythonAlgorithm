import sys
input = sys.stdin.readline

n = int(input())
a = input().strip()
aa,bb = 0,0
for i in range(n):
  if a[i] == 'A':
    aa += 1
  elif a[i] == 'B':
    bb += 1

if aa > bb:
  print('A')
elif aa < bb:
  print('B')
elif aa == bb:
  print('Tie')