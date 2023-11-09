import sys
input = sys.stdin.readline

n = int(input())
ice = list(map(int,input().split()))
ans = {} # 현재 아이스크림

def plus(): # 목록 b에 있는 아이스크림을 넣어주는 함수
  for i in range(1,len(b)): # dic2에 ans에 다시 넣어줄 구슬 저장 
    if b[i] in dic2:
      dic2[b[i]] += 1
    else:
      dic2[b[i]] = 1
  for x in dic2: # 그 구슬이 ans안에 있으면 + 해주고, 없으면 추가 
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
  dic1 = {} # 먹을 구슬 저장 
  dic2 = {} # 다시 넣어줄 구슬 저장 
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))

  if a[0] == 0: # 먹을 구슬이 없으면 넣기만 함
    plus()
  else:
    for i in range(1,len(a)): # dic1에 먹을 구슬 저장 
      if a[i] in dic1:
        dic1[a[i]] += 1
      else:
        dic1[a[i]] = 1
    for x in dic1: 
      if x not in ans or dic1[x] > ans[x]: # 아이스크림에 해당 구슬이 존재하고, 그 양이 먹을 구슬보다 작다면
        break # 다 못먹으니까 break
    else: # for ~ else문 활용
      for x in dic1: # 다 먹고
        ans[x] -= dic1[x]
      plus() # 아이스크림에 b 구슬 다시 넣어줌 

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
