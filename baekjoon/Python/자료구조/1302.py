import sys
input = sys.stdin.readline

n = int(input())
dict = {}
ans = []

for _ in range(n):
  a = input().strip()
  if a in dict:
    dict[a] += 1
  else:
    dict[a] = 1

for k,v in dict.items():
  if v == max(dict.values()):
    ans.append(k)

ans.sort()
print(ans[0])