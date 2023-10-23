import sys
input = sys.stdin.readline

n = int(input())
m = []
for _ in range(n):
  m.append(int(input()))

m.sort(reverse=True)
ans = 0

for i in range(2,n,3): # 무료인 것 골라주기
  ans += m[i]

print(sum(m) - ans)