import sys
input = sys.stdin.readline

n = int(input())
graph = [['.' for _ in range(n)] for _ in range(n)]
a = input()

x,y = 0,0
for i in a:
  if i == 'D':
    if x + 1 >= n :
      continue
    else:
      if graph[x][y] == '.':
        graph[x][y] = '|' 
      elif graph[x][y] == '-':
        graph[x][y] = '+'
      x += 1
      if graph[x][y] == '.':
        graph[x][y] = '|' 
      elif graph[x][y] == '-':
        graph[x][y] = '+'

  elif i == 'R':
    if y + 1 >= n:
      continue
    else:
      if graph[x][y] == '.':
        graph[x][y] = '-' 
      elif graph[x][y] == '|':
        graph[x][y] = '+'
      y += 1
      if graph[x][y] == '.':
        graph[x][y] = '-' 
      elif graph[x][y] == '|':
        graph[x][y] = '+'
      
  elif i == 'U':
    if x - 1 < 0 :
      continue
    else:
      if graph[x][y] == '.':
        graph[x][y] = '|' 
      elif graph[x][y] == '-':
        graph[x][y] = '+'
      x -= 1
      if graph[x][y] == '.':
        graph[x][y] = '|' 
      elif graph[x][y] == '-':
        graph[x][y] = '+'

  elif i == 'L':
    if y - 1 < 0:
      continue
    else:
      if graph[x][y] == '.':
        graph[x][y] = '-' 
      elif graph[x][y] == '|':
        graph[x][y] = '+'
      y -= 1
      if graph[x][y] == '.':
        graph[x][y] = '-' 
      elif graph[x][y] == '|':
        graph[x][y] = '+'
      
for x in graph:
  print(''.join(map(str,x)))