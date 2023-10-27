import sys
input = sys.stdin.readline

n = int(input())
dic = {'ChongChong':1}
ans = 0
for _ in range(n):
  a,b = input().split()
  if a in dic or b in dic:
    dic[a] = 1
    dic[b] = 1

for k in dic.values():
  if k != 0 :
    ans += 1

print(ans)
  