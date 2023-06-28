import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
cnt = 0 

for x in a:
  if x == 10:
    cnt += 1
  else:
    if x % 10 != 0:
      for i in range(x // 10 - 1):
        if m == 0:
          break
        else:
          m -= 1
          cnt += 1
    else:
      for i in range(x // 10 - 1 ):
        if m == 0:
          break
        else:
          m -= 1
          cnt += 1
      cnt += 1


      

print(cnt)
