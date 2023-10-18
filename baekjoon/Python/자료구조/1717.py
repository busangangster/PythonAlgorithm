import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())
parent =[x for x in range(n+1)]

def find(x):
  if x == parent[x]:
    return x

  parent[x] = find(parent[x])
  return parent[x]

def union(x,y):
  x = find(x)
  y = find(y)

  if x < y:
    parent[y] = x
  else:
    parent[x] = y

for _ in range(m):
  c,a,b = map(int,input().split())
  if not c:
    union(a,b)
  else:
    if find(a) == find(b):
      print('YES')
    else:
      print('NO')