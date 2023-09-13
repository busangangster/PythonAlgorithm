import sys
input = sys.stdin.readline

a = [list(map(int,input().split())) for _ in range(5)]
mc = []
cnt = 0
for _ in range(5):
  mc += list(map(int,input().split()))

def check():
  bingo = 0

  for x in a: # 가로
    if x.count(0) == 5:
      bingo += 1
  
  for i in range(5): # 세로
    s = 0
    for j in range(5):
      if a[j][i] == 0:
        s += 1
    if s == 5:
      bingo += 1

  s1 = 0
  for i in range(5):
    if a[i][i] == 0:
      s1 += 1
  if s1 == 5:
    bingo += 1

  s2 = 0
  for i in range(5):
    if a[i][4-i] == 0:
      s2 += 1
  if s2 == 5:
    bingo += 1
  
  return bingo

for i in range(25):
  for j in range(5):
    for k in range(5):
      if mc[i] == a[j][k]:
        a[j][k] = 0
        cnt += 1

  if cnt >= 12:
    result = check()

    if result >= 3:
      print(i+1)
      break