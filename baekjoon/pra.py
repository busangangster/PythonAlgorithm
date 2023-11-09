import sys
input = sys.stdin.readline

n = int(input())
ice = list(map(int,input().split()))
ans = {}

def plus():
  for x in dic1:
    ans[x] -= dic1[x]
  for i in range(1,len(b)):
    if b[i] in dic2:
      dic2[b[i]] += 1
    else:
      dic2[b[i]] = 1
  for x in dic2:
    if x in ans:
      ans[x] += dic2[x]
    else:
      ans[x] = dic2[x]

  return ans

for x in ice:
  if x in ans:
    ans[x] += 1
  else:
    ans[x] = 1

q = int(input())
for _ in range(q):
  dic1 = {}
  dic2 = {}
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))
  if a[0] == 0:
    plus()
    
  else:
    for i in range(1,len(a)):
      if a[i] in dic1:
        dic1[a[i]] += 1
      else:
        dic1[a[i]] = 1
    for x in dic1:
      if x not in ans or dic1[x] > ans[x]:
        break
    else:
      plus()

cnt = 0
k = []
for x,y in ans.items():
  if y != 0:
    for _ in range(y):
      k.append(x)
      cnt += 1

if cnt == 0:
  print(cnt)
else:
  print(cnt)
  print(*k)
    