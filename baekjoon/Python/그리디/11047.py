import sys
n,k = map(int,sys.stdin.readline().split())
a= []

for _ in range(n):
  tmp = int(sys.stdin.readline())
  a.append(tmp)
a.sort(reverse = True)

cnt = 0

for i in a:
  cnt += k // i
  k = k % i

print(cnt)