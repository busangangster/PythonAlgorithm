import sys
input = sys.stdin.readline

t = int(input())

for i in range(1,t+1):
  a = list(map(int,input().split()))
  cnt = 0
  for i in range(1,20):
    for j in range(i+1,21):
      if a[i] > a[j]:
        a[i],a[j] = a[j],a[i]
        cnt += 1

  print(a[0],cnt)