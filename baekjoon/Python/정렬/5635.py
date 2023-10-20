import sys
input = sys.stdin.readline

n = int(input())
p = []
for _ in range(n):
  a,b,c,d = input().split()
  p.append([a,int(b),int(c),int(d)])

p.sort(key = lambda x:(x[3],x[2],x[1]))
print(p[-1][0])
print(p[0][0])