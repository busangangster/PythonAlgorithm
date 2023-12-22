import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  dic = {}
  s = list(input().strip().split(" "))
  others = []
  while True:
    k = input().strip()
    if k == "what does the fox say?":
      break
    else:
      t = list(k.split(" "))
      others.append(t[2])
  for x in s:
    if x in others:
      continue
    else:
      print(x,end=' ') 
 