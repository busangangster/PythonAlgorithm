import sys
input = sys.stdin.readline

dic = {}
dic2 = {}
for _ in range(3):
  a,b = map(int,input().split())
  if a in dic:
    dic[a] += 1
  else:
    dic[a] = 1
  
  if b in dic2:
    dic2[b] += 1
  else:
    dic2[b] = 1

for x,y in dic.items():
  if y == 1:
    print(x,end=' ')
for x,y in dic2.items():
  if y == 1:
    print(x)