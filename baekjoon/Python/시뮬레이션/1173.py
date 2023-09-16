import sys
input = sys.stdin.readline

N,m,M,T,R = map(int,input().split())
cnt = 0
ex = 0
time = m

if m + T > M:
  print(-1)
  sys.exit()
else:
  while ex < N:
    if time + T <= M:
      time += T
      ex += 1
      cnt += 1
    else:
      time -= R
      if time < m:
        time = m
      cnt += 1

print(cnt)