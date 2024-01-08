t = int(input())
for tc in range(1,t+1):
  n,m = map(int,input().split())
  arr = [list(map(int,input().split())) for _ in range(n)]
  result = []

  plus_x = [-1,0,1,0]
  plus_y = [0,1,0,-1]

  x_x = [-1,-1,1,1]
  x_y = [-1,1,-1,1]

  for i in range(n):
    for j in range(n):
      ans = arr[i][j]
      for x in range(1,m):
        for z in range(4):
          xx = i+plus_x[z]*x
          yy = j+plus_y[z]*x
          if 0 <= xx < n and 0 <= yy <n:
            ans += arr[xx][yy]
      result.append(ans)

  for i in range(n):
    for j in range(n):
      ans = arr[i][j]
      for x in range(1,m):
        for z in range(4):
          xx = i+x_x[z]*x
          yy = j+x_y[z]*x
          if 0 <= xx < n and 0 <= yy <n:
            ans += arr[xx][yy]
      result.append(ans)
  # print(result)
  print('#{} {}'.format(tc,max(result)))
  
          
