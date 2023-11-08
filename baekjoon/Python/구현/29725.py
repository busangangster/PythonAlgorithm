import sys
input = sys.stdin.readline

graph = [list(input().strip()) for _ in range(8)]
black = 0
white = 0
dic = {'k':0,'K':0,'p':1,'P':1,'N':3,'n':3,
       'B':3,'b':3,'R':5,'r':5,'Q':9,'q':9}

for i in range(8):
  for j in range(8):
    if graph[i][j] != '.':
      if graph[i][j].isupper():
        white += dic[graph[i][j]]
      elif graph[i][j].islower():
        black += dic[graph[i][j]]

print(white-black)