import sys
input = sys.stdin.readline

n = int(input())
t = []
for _ in range(n):
  a,b = map(str,input().split())
  b = int(b)
  t.append([a,b])
  
t.sort(key = lambda x:x[1])
print(t[0][0])