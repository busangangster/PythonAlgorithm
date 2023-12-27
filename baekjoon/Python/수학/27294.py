import sys
input = sys.stdin.readline

n,m = map(int,input().split())
k = [12,13,14,15,16]
if m == 1 or n not in k:
  print(280)
elif n in k and m == 0:
  print(320)