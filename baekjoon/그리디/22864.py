import sys
input = sys.stdin.readline

a,b,c,m = map(int,input().split())
ans = 0 # 한 일
tired= 0 # 피로도
clock = 1 # 1시부터

if a > m:
  print(0)
else:
  while clock <= 24: # 24시까지 
    if tired + a > m: # 피로도가 max를 안넘으면(같아도 됨)
      if tired-c < 0: # 휴식을 취할 때 피로도가 음수가 되는지
        tired = 0
      else:
        tired -= c
    else:
      tired += a
      ans += b
    clock += 1 # 시간은 1시간씩 증가
  print(ans)

