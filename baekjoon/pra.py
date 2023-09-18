import sys
input = sys.stdin.readline

a = list(map(int,input().strip()))
b = list(map(int,input().strip()))

g = []
ans = []

for i in range(8):
  for j in range(i,i+1):
    ans.append(a[i])
    ans.append(b[j])

while len(ans) > 2:
  g = ans
  ans = []
  for i in range(1,len(g)):
    ans.append((g[i-1]+g[i]) % 10) 

t = str(ans[0]) + str(ans[1])

if len(t) == 2 and int(t) %10 == 0:
  print(t)
elif len(t) == 1 and int(t) % 10 == 0:
  print('0' + t)
else:
  print(t)