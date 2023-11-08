import sys
input = sys.stdin.readline

S = list(input().strip())
T = list(input().strip())
ans = 0
def DFS(t):
  global ans
  if t == S:
    ans = 1
    return
  
  if len(t) == 0:
    return 
  
  if t[-1] == 'A':
    DFS(t[:-1])
  
  if t[0] == 'B':
    DFS(t[1:][::-1])
    
DFS(T)
print(ans)

