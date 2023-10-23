import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = []
dic = {}

for i in b:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1

for i in a:
  if i in dic:
    continue
  else:
    ans.append(i)

if ans != []:
  print(len(ans))
  ans.sort()
  print(*ans)
else:
  print(0)