import sys
input = sys.stdin.readline

n = int(input())
ans = []

def DFS():
  if len(ans) == n:
    print(*ans)
    return
  for i in range(1,n+1):
    if i not in ans:
      ans.append(i)
      DFS()
      ans.pop()

DFS()