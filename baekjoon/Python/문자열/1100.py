import sys
input = sys.stdin.readline
a = [0,1,0,1,0,1,0,1]
b = [1,0,1,0,1,0,1,0]

graph = [list(input().strip()) for _ in range(8)]
cnt = 0

for i in range(8):
  for j in range(8):
    if i % 2 != 0:
      if b[j] == 0 and graph[i][j] == 'F':
        cnt += 1

    else:
      if a[j] == 0 and graph[i][j] == 'F':
        cnt += 1
print(cnt)