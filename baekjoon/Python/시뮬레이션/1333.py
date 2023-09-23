import sys
input = sys.stdin.readline

n,l,d = map(int,input().split())

total = n*l + (n-1)*5
ans = [False] * total
for i in range(0,total,l+5):
  for j in range(i,i+l):
    ans[j] = True

for i in range(0,total,d):
  if not ans[i]:
    print(i)
    break
else:
  print(i+d)


  


