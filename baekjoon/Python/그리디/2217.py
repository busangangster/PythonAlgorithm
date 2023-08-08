import sys
input = sys.stdin.readline


n = int(input())
roops = []
ans = []
for _ in range(n):
  a = int(input())
  roops.append(a)

roops.sort(reverse=True)
for i in range(n):
  ans.append(roops[i]* (i+1))

print(max(ans))









