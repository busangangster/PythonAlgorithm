import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
s = int(input())

for i in range(n):
  mx = max(a[i:min(n, i+s+1)])
  idx = a.index(mx)

  for j in range(idx,i,-1):
    a[j],a[j-1] = a[j-1],a[j]

  s -= (idx - i)
  if s <= 0:
    break
  
print(*a)

        