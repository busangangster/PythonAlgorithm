import sys
input = sys.stdin.readline

n = input().strip()
time = 0
cur = 'A' # 시작점은 A 

for x in n:
  t = ord(cur) - ord(x) # 왼쪽으로 도는경우
  k = ord(x) - ord(cur) # 오른쪽으로 도는 경우
  # 어느 쪽으로 도는게 더 짧은지 비교
  if t < 0: 
    t += 26 # 알파벳을 한바퀴 돌기 위해서는 26번 이동해야 하기에 + 26
  elif k < 0:
    k += 26
  print(t,k)
  cur = x # 이동한 위치로 설정 
  time += min(t,k) # t,k 중 더 작은 값을 time에 더해줌 

print(time)



