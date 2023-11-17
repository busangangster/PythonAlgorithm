t = int(input())
 
nx = [0,1,0,-1]
ny = [1,0,-1,0]
 
for t_case in range(1,t+1):
  n = int(input())
  graph = [[0 for _ in range(n)] for _ in range(n)]
  r,c = 0,0
  s = 0

  for i in range(1,n*n+1):
    graph[r][c] = i

    if i == n*n:
      break

    while True:
      x,y = r + nx[s], c + ny[s]
      if (0 <= x < n) and (0 <= y < n) and graph[x][y] == 0:
          break
      else:
          s = (s+1) % 4

    r,c = r + nx[s], c + ny[s]

print('#{}'.format(t_case))
for x in graph:
    print(*x)