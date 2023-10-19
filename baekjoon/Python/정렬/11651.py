import sys
input = sys.stdin.readline

n = int(input())
k = []
for _ in range(n):
  a,b = map(int,input().split())
  k.append([a,b])

k.sort(key = lambda x:(x[1],x[0]))
for a,b in k:
  print(a,b)