import sys
input = sys.stdin.readline

s = input().rstrip()
ans = 0

for i in range(len(s)-1):
  if s[i] != s[i+1]:
    ans += 1

print((ans+1)//2)