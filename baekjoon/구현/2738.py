

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
first = []
second = []

for i in range(n):
  first.append(list(map(int,input().split())))

for i in range(n):
  second.append(list(map(int,input().split())))

for i in range(n):
  for j in range(m):
    print(first[i][j] + second[i][j],end=' ')
  print()

  
  