import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
cnt_a = 0
cnt_b = 0
ans = 0

for i in range(n):
  if a[i] == 1 and b[i] == 2:
    cnt_a = 0
    cnt_b += 1
  elif a[i] == 2 and b[i] == 3:
    cnt_a = 0
    cnt_b += 1
  elif a[i] == 3 and b[i] == 1:
    cnt_a = 0
    cnt_b += 1
  elif a[i] == 2 and b[i] == 1:
    cnt_a += 1
    cnt_b = 0
  elif a[i] == 3 and b[i] == 2:
    cnt_a += 1
    cnt_b = 0
  elif a[i] == 1 and b[i] == 3:
    cnt_a += 1
    cnt_b = 0
  elif a[i] == b[i]:
    if cnt_b == 0:
      cnt_a = 0
      cnt_b += 1
    else:
      cnt_a += 1
      cnt_b = 0
  # print(cnt_a,cnt_b)
  
  ans = max([ans,cnt_a,cnt_b])

print(ans)