import sys
input = sys.stdin.readline

while True:
  n,m = map(int,input().split())
  cnt = 0
  if n == 0 and m == 0:
    break
  dic = {}
  for _ in range(n):
    a = int(input())
    if a in dic:
      dic[a] += 1
    else:
      dic[a] = 1
  
  for _ in range(m):
    a = int(input())
    if a in dic:
      dic[a] += 1
    else:
      dic[a] = 1
  
  for k,v in dic.items():
    if v == 2:
      cnt += 1
      
  print(cnt)