import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
parent =[x for x in range(n+1)]
cost = [0] + list(map(int,input().split()))

def find(t):
  if t == parent[t]:
    return t
  else:
    parent[t] = find(parent[t])
    return parent[t]
  
def union(a,b):
  a = find(a)
  b = find(b)

  if cost[a] <= cost[b]:
    parent[b] = a
  else:
    parent[a] = b
  
for _ in range(m):
  v,w = map(int,input().split())
  union(v,w)

ans = 0
for i,v in enumerate(parent):
  if i == v:
    ans += cost[i]

if ans <= k:
  print(ans)
else:
  print("Oh no")
