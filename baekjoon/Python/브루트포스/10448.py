import sys
input = sys.stdin.readline
t = int(input())
arr = [i*(i+1) // 2 for i in range(1,46)]
cnt = [0 for _ in range(1001)]
for x in arr:
  for y in arr:
    for z in arr:
      result = x+y+z
      if result <= 1000:
        cnt[result] = 1

for _ in range(t):
  n = int(input())
  print(cnt[n])