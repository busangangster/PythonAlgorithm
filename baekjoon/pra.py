import sys
input = sys.stdin.readline

n = int(input())
a = input().strip()
cnt = 0
dic = {}
for i in a:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1

print(dic)
    
for _ in range(n-1):
  t = input().strip()

  if len(t) > len(a):
    if len(t)-len(a) > 1:
      continue
  if len(a) > len(t):
    if len(a)-len(t) > 1:
      continue
  
  for i in t:
    if i in dic:
      dic[i] += 1
    else:
      dic[i] = 1
  
  for k,v in dic.items():
    if v 
  