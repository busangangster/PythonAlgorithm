import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  a = list(map(int,input().split()))
  k = []
  for x in a:
    if x % 2 == 0:
      k.append(x)
  
  k.sort()
  print(sum(k),k[0])