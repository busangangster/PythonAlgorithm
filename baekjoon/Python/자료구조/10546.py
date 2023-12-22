import sys
input = sys.stdin.readline

n = int(input())
dic ={}
for _ in range(n):
  s = input().strip()
  if s in dic:
    dic[s] += 1
  else:
    dic[s] = 1

for _ in range(n-1):
  s = input().strip()
  if s in dic:
    dic[s] -= 1

for x,y in dic.items():
  if y != 0:
    print(x)
    break