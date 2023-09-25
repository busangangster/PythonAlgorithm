import sys
input = sys.stdin.readline

a = list(input().strip())
c = [0,1,0,0,2]
small = 0
big = 0

for i in a:
  if i == 'A':
    c[1],c[2] = c[2],c[1]
  elif i == 'B':
    c[1],c[3] = c[3],c[1]
  elif i == 'C':
    c[1],c[4] = c[4],c[1]
  elif i == 'D':
    c[2],c[3] = c[3],c[2]
  elif i == 'E':
    c[2],c[4] = c[4],c[2]
  else:
    c[3],c[4] = c[4],c[3]

for i in range(1,len(c)):
  if small != 0 and big != 0:
    break
  else:
    if c[i] == 1:
      small = i
    elif c[i] == 2:
      big = i

print(small)
print(big)