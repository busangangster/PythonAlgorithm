import sys
input = sys.stdin.readline

a,b,v = map(int,input().split())
k = (v-b)/(a-b)
if k == int(k):
  print(int(k))
else:
  print(int(k)+1)