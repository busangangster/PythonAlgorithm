import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  a = list(map(int,input().split()))
  cnt = 0
  k = [0] * n
  
  while True:
    a = [i if i %2 == 0 else i+1 for i in a] # 리스트 컴프리헨션
    if len(set(a)) == 1:
      break
    else:
      for i in range(n):
        t = a[i] // 2
        k[i] = t
        a[i] = a[i] - t
      for i in range(n):
        if i == n-1:
          a[0] = a[0] + k[i]
        else:
          a[i+1] = a[i+1] + k[i]
      cnt += 1
  print(cnt)