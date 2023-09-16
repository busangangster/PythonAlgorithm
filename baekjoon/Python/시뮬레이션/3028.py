import sys
input = sys.stdin.readline

a = list(input().strip())
cups = [[1],[0],[0]]

for i in a:
  if i == 'A':
    cups[0],cups[1] = cups[1],cups[0]

  elif i == 'B':
    cups[1],cups[2] = cups[2],cups[1]

  else:
    cups[0],cups[2] = cups[2],cups[0]

for i in range(3):
  if cups[i][0] == 1:
    print(i+1)

