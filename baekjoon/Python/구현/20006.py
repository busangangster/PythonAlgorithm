import sys
input = sys.stdin.readline

p,m = map(int,input().split())
room = [] 

for _ in range(p):
  l,n = list(input().split())
  l = int(l)
  if room == []: # 방이 아예 없으면 하나 만듦
    room.append([(l,n)])

  else:
    for x in room: # 조건 1,2를 다 만족하면, 해당 방에 입장 가능
      if (x[0][0] - 10 <= l <= x[0][0] + 10) and len(x) < m:
        x.append((l,n))
        break
    else: # 하나라도 만족 못하면 새로운 방 생성 
      room.append([(l,n)])

for x in room:
  x.sort(key = lambda x: x[1]) # 닉네임순으로 오름차순 정렬
  if len(x) == m: # 방이 다 찬 경우
    print('Started!')
    for i,j in x:
      print(i,j)
  else: # 방이 다 차지 않은 경우
    print('Waiting!')
    for i,j in x:
      print(i,j)