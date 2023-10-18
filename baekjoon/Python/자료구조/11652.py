import sys
input = sys.stdin.readline

n = int(input())
ans = []
dic = {}
for _ in range(n):
  a = int(input())
  if a in dic:
    dic[a] += 1
  else:
    dic[a] = 1

dd = sorted(dic.items(),key = lambda x: (-x[1], x[0]))
print(dd[0][0])