
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
p = dict()
ans = []
for i in range(n):
  word = input().strip()
  p[word] = 1

for i in range(m):
  word = input().strip()
  if word in p.keys():
    p[word] = 2

for key,val in p.items():
  if val == 2:
    ans.append(key)

print(len(ans))
ans.sort()
for x in ans:
  print(x)


    
    