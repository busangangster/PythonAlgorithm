t = int(input())
for tc in range(1,t+1):
  arr = [list(map(int,input().split())) for _ in range(9)]

  ans = 1
  for i in range(9):
    a = [0]*10
    b = [0]*10
    for j in range(9):
      a[arr[i][j]] += 1
      b[arr[j][i]] += 1
    
    for x in range(1,10):
      if a[x] != 1:
        ans = 0
        break
      if b[x] != 1:
        ans = 0
        break
  
  for i in range(3):
    for j in range(3):
      c = [0]*10
      for x in range(3):
        for z in range(3):
          c[arr[3*i+x][3*j+z]] += 1
      
      for p in range(1,10):
        if c[p] != 1:
          ans = 0
          break
  
  print('#{} {}'.format(tc,ans))