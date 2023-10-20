import sys
input = sys.stdin.readline

n,k = map(int,input().split())
countries = []
for _ in range(n):
  countries.append(list(map(int,input().split())))
cur = 0

countries.sort(key = lambda x: (-x[1],-x[2],-x[3]))
for i in range(n):
  if countries[i][0] == k:
    cur = i

for i in range(n):
  if countries[cur][1:] == countries[i][1:]:
    print(i+1)
    break
