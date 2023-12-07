def DFS(idx,ans):
  global cnt
  if ans == k:
    cnt += 1
    return 
  
  if idx == n:
    return 
  
  DFS(idx+1,ans+a[idx])
  DFS(idx+1,ans)
  

t = int(input())
for tc in range(1,t+1):
  n,k = map(int,input().split())
  a = list(map(int,input().split()))
  cnt = 0 
  DFS(0,0)
  print('#{} {}'.format(tc,cnt))