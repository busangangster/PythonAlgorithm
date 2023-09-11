import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ans = []

def DFS():
  if len(ans) == m:
    print(*ans)
    return 
  
  else:
    for i in range(1,n+1):
      if i not in ans:
        ans.append(i)
        DFS()
        ans.pop()
      
DFS()