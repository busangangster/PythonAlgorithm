
def DFS(index,score,total_k):
  global max_score

  if total_k > l:
    return
  if max_score < score:
    max_score = score
    
  if index == n:
    return 

  i_score,i_k = ingredient[index]

  DFS(index+1,i_score + score,total_k + i_k)
  DFS(index+1,score,total_k)

t = int(input())
for t_case in range(1,t+1):
  n,l = map(int,input().split())
  ingredient = []
  for _ in range(n):
    a,b = map(int,input().split())
    ingredient.append([a,b])
  max_score = 0
  DFS(0,0,0)
  print('#{} {}'.format(t_case,max_score))