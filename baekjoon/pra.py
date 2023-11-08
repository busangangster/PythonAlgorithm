import sys
input = sys.stdin.readline

nx = [2,0,-2,0]
ny = [0,2,0,-2]

n,k = map(int,input().split())

da = []
cnt = 0
dic = {}
for _ in range(k):
  x,y = map(int,input().split())
  dic[(x,y)] = -1

  for i in range(4):
    xx = x + nx[i]
    yy = y + ny[i]
    if (0< xx <=n) and (0 < yy <= n):
      if (xx,yy) in dic and dic[(xx,yy)] == -1:
        continue
      elif (xx,yy) in dic :
          dic[(xx,yy)] += 1
      else:
        dic[(xx,yy)] = 1

print(dic)
for x,y in dic.items():
  if y != -1:
    cnt += 1
print(cnt)