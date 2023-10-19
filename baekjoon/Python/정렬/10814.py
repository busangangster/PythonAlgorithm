import sys
input = sys.stdin.readline

n = int(input())
k = [[] for _ in range(201)]
for _ in range(n):
  a = list(input().split())
  k[int(a[0])].append(a[1])

for i in range(1,len(k)):
  if not k[i]:
    continue
  else:
    for j in range(len(k[i])):
      print(i,k[i][j], sep=' ')


