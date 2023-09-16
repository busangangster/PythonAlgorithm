import sys
input = sys.stdin.readline

n = int(input())
ball = [[10],[1],[0],[0]]
for _ in range(n):
  a,b = map(int,input().split())
  ball[a], ball[b] = ball[b],ball[a]

for i in range(1,4):
  if ball[i][0] == 1:
    print(i)
