import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
ans = []
left,right,mid,l_leg,r_leg = 0,0,0,0,0
body = []

for i in range(n):
  for j in range(n):
    if graph[i][j] == '*':
      x,y = i+1,j
      ans.append([x,y])
      break

print(ans[0][0]+1,ans[0][1]+1)

x = ans[0][0]
y = ans[0][1]
while y >= 0 and graph[x][y] == '*':
  left += 1
  y -= 1
body.append(left-1)

x = ans[0][0]
y = ans[0][1]
while y < n and graph[x][y] == '*':
  right += 1
  y += 1
body.append(right-1)

x = ans[0][0]
y = ans[0][1]
while x < n and graph[x][y] == '*':
  mid += 1
  x += 1
  k = x
body.append(mid-1)

x = k 
y = ans[0][1] -1 
while x < n and graph[x][y] == '*':
  l_leg += 1
  x += 1
body.append(l_leg)

x = k 
y = ans[0][1] + 1
while x < n and graph[x][y] == '*':
  r_leg += 1
  x += 1
body.append(r_leg)

print(*body)