import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
max_v = -2147000000
min_v = 2147000000

def DFS(depth,total,plus,minus,multiply,divide):
  global max_v,min_v
  if depth == n:
    max_v = max(max_v,total)
    min_v = min(min_v,total)
  else:
    if plus:
      DFS(depth+1,total+a[depth],plus-1,minus,multiply,divide)
    if minus:
      DFS(depth+1,total-a[depth],plus,minus-1,multiply,divide)
    if multiply:
      DFS(depth+1,total*a[depth],plus,minus,multiply-1,divide)

    if divide:
      if total <0:
        DFS(depth+1,(-total//a[depth])*-1,plus,minus,multiply,divide-1)
      else:
        DFS(depth+1,total//a[depth],plus,minus,multiply,divide-1)

DFS(1,a[0],b[0],b[1],b[2],b[3])
print(max_v)
print(min_v)