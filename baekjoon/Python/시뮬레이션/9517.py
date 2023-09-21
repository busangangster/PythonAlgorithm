import sys
input = sys.stdin.readline

k = int(input())
n = int(input())
people = [x for x in range(1,9)]
q = []
time = 0
for _ in range(n):
  a,b = map(str,input().split())
  q.append([a,b])

p = k
for i in q:
  if i[1] == 'T':
    time += int(i[0])
    if time >= 210:
      print(p)
      break
    else:
      if p == 8:
        p = 1
      else:
        p += 1

  elif i[1] == 'P' or i[1] == 'N':    
    time += int(i[0])
    if time >= 210:
      print(p)
      break