import sys
input = sys.stdin.readline

num = list(map(int,input().split()))
ans = 1
while True:
  cnt = 0
  for i in num:
    if ans % i == 0:
      cnt += 1

  if cnt >= 3:
    print(ans)
    break
  ans += 1