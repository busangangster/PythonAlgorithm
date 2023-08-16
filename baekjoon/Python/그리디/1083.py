import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
s = int(input())

for i in range(n):
  cur = a[i]
  t = 0
  if s == 0:
    break
  else:
    for j in range(i,n):
      if a[j] > cur:
        cur = a[j]
        t += 1
        

    
      

        

