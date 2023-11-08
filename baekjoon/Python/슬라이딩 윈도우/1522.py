import sys
input = sys.stdin.readline

s = input().strip()
t = len(s)
min_v = 2147000000
a = s.count('a')
s += s[:a-1]

for i in range(t):
  ans = s[i:i+a].count('b')
  min_v = min(min_v,ans)

print(min_v)