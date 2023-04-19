import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
dy = [[0] * (len(b)+1) for _ in range(len(a)+1)]

for i in range(1,len(a)+1):
  for j in range(1,len(b)+1):
    if a[i-1] == b[j-1]:
      dy[i][j] = dy[i-1][j-1] + 1
    else:
      dy[i][j] = max(dy[i-1][j],dy[i][j-1])

print(dy[-1][-1])
                 
