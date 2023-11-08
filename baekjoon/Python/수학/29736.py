

import sys
input = sys.stdin.readline
a,b = map(int,input().split())
k,x = map(int,input().split())

t = [x for x in range(a,b+1)] # 실력이 비슷한 사람들이 푼 문제수
cnt = 0

for i in range(k-x,k+x+1): # 친구 자격을 갖춘 사람을 찾음 
  if i in t: 
    cnt += 1

if cnt == 0:
  print('IMPOSSIBLE')
else:
  print(cnt)



