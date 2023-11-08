import sys
input = sys.stdin.readline

nx = [2,0,-2,0]
ny = [0,2,0,-2]
n,k = map(int,input().split())

cnt = 0
dic = {}
for _ in range(k):
  x,y = map(int,input().split())
  dic[(x,y)] = -1 # 기물이 있는 위치면 딕셔너리 값을 -1로

  for i in range(4): # 상하좌우 탐색
    xx = x + nx[i]
    yy = y + ny[i]
    if (0< xx <=n) and (0 < yy <= n): # 체스판을 넘어가지 않으면서
      if (xx,yy) in dic and dic[(xx,yy)] == -1: # 기물이 있는 위치라면 못감
        continue 
      elif (xx,yy) in dic : # 기물이 없는 위치 == 갈 수 있는 위치
          dic[(xx,yy)] += 1 # 해당 값 1 증가
      else: # 이동하려는 칸이 처음 등장했을 때
        dic[(xx,yy)] = 1

for x,y in dic.items():
  if y != -1: 
    cnt += 1

print(cnt)