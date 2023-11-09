import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  a,b = input().split()
  b = list(b)
  b.pop(int(a)-1)
  print(''.join(map(str,b)))