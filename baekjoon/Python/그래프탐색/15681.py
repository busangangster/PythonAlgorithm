import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS(x):
  count[x] = 1 # 자기 자신도 서브트리에 포함되기에 1에서 시작 
  for k in tree[x]:
    if not count[k]:
      DFS(k)
      count[x] += count[k] # DFS가 종료되었을 때, 자신을 루트로 하는 서브트리를 더해줌

n,r,q = map(int,input().split())
tree = [[] for _ in range(n+1)]
count = [0] * (n+1) # count 리스트를 0으로 초기화해서 방문여부 + 정점의 수 확인 

for _ in range(n-1):
  u,v = map(int,input().split())
  tree[u].append(v)
  tree[v].append(u)

DFS(r)

for _ in range(q):
  ans = int(input())
  print(count[ans])


