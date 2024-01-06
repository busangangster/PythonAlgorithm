t = int(input())
for tc in range(1,t+1):
  n = int(input())
  arr = [list(map(int,input().split())) for _ in range(n)]
  arr90 = [[0 for _ in range(n)] for _ in range(n)]
  arr180 = [[0 for _ in range(n)] for _ in range(n)]
  arr270 = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      arr90[i][j] = arr[n-1-j][i]
  
  for i in range(n):
    for j in range(n):
      arr180[i][j] = arr90[n-1-j][i]

  for i in range(n):
    for j in range(n):
      arr270[i][j] = arr180[n-1-j][i]

  print('#{}'.format(tc))
  for i in range(n):
    print(''.join(map(str,arr90[i])),end=' ')
    print(''.join(map(str,arr180[i])),end=' ')
    print(''.join(map(str,arr270[i])))
    