import sys
input = sys.stdin.readline

s = []
k = [0] * 151
ans = []
score = 0
for i in range(1,9):
  a = int(input())
  s.append(a)
  k[a] = i

s.sort(reverse=True)

for i in range(5):
  score += s[i]
  ans.append(k[s[i]])
ans.sort()
print(score)
print(*ans)