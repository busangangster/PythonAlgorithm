import sys
input = sys.stdin.readline

n = int(input())
baekjoon = []
others = []
for _ in range(n):
  a = input().strip()
  if a[:6] == 'boj.kr':
    baekjoon.append(a)
  else:
    others.append(a)

others.sort(key = lambda x:(len(x),x))

r = []
for x in baekjoon:
  s = x.split('/')
  r.append(s)

r.sort(key = lambda x:int(x[1]))
for x in others:
  print(x)

for x in r:
  t = '/'.join(map(str,x))
  print(t)
