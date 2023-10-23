import sys
input = sys.stdin.readline

n = int(input())
f = []
dic = {}
for _ in range(n):
  k = input().strip()
  f.append(k.split('.'))

for i in f:
  if i[1] in dic:
    dic[i[1]] += 1
  else:
    dic[i[1]] = 1

ans = sorted(dic.items(), key = lambda x:x[0])

for a,b in ans:
  print(a,b,sep=' ')