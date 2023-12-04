import sys
input = sys.stdin.readline

def gcd(a,b):
  while b > 0:
    a,b = b,a%b
  return a

n = int(input())
tree = []
dis = []
cnt = 0
for _ in range(n):
  tree.append(int(input()))

for i in range(n-1):
  dis.append(abs(tree[i]-tree[i+1]))

g = dis[0]
for i in range(1,len(dis)):
  g = gcd(g,dis[i])

for x in dis:
  cnt += x // g -1

print(cnt)

