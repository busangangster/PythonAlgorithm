import sys
input = sys.stdin.readline

m = ['a','e','i','o','u']
a = input()
cnt = 0
for x in a:
  if x in m:
    cnt += 1
print(cnt)