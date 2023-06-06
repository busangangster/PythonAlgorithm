

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
k = {}

for x in a:
  if x in k:
    k[x] += 1
  else:
    k[x] = 1

for i in b:
  if i in k:
    print(k[i],end=' ')
  else:
    print(0,end=' ')




    

