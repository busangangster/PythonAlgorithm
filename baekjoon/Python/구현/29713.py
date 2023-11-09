import sys
input = sys.stdin.readline

n = int(input())
a = list(input().strip())
d = 'BRONZESILVER'
cnt = 0
dic = {}
for x in a:
  if x in dic:
    dic[x] += 1
  else:
    dic[x] = 1
while True:
  for x in d:
    if x in dic:
      if x == 'B':
        if dic[x] >= 1:
          dic[x] -= 1
        else:
          print(cnt)
          sys.exit()
      elif x == 'R':
        if dic[x] >= 1:
          dic[x] -= 1
        else:
          print(cnt)
          sys.exit()
      elif x == 'O':
        if dic[x] >= 1:
          dic[x] -= 1
        else:
          print(cnt)
          sys.exit()
      elif x == 'N':
        if dic[x] >= 1:
          dic[x] -= 1
        else:
          print(cnt)
          sys.exit()
      elif x == 'Z':
        if dic[x] >= 1:
          dic[x] -= 1
        else:
          print(cnt)
          sys.exit()
      elif x == 'E':
        if dic[x] >= 1:
          dic[x] -= 1
        else:
          print(cnt)
          sys.exit()
      elif x == 'S':
        if dic[x] >= 1:
          dic[x] -= 1
        else:
          print(cnt)
          sys.exit()
      elif x == 'I':
        if dic[x] >= 1:
          dic[x] -= 1
        else:
          print(cnt)
          sys.exit()
      elif x == 'L':
        if dic[x] >= 1:
          dic[x] -= 1
        else:
          print(cnt)
          sys.exit()
      elif x == 'V':
        if dic[x] >= 1:
          dic[x] -= 1
        else:
          print(cnt)
          sys.exit()
    else:
      print(cnt)
      sys.exit()
  cnt += 1