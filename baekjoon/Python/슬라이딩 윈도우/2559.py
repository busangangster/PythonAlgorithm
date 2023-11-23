import sys
input = sys.stdin.readline
n,k = map(int,input().split())
a = list(map(int,input().split()))

window = sum(a[:k])
result = window 

for i in range(n-k):
  window -= a[i]
  window += a[i+k]
  result = max(result,window)

print(result)
  