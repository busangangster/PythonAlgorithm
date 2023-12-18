import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  a,b = map(str,input().split())
  dic = {}
  for x in a:
    if x in dic:
      dic[x] += 1
    else:
      dic[x] = 1
  for x in b:
    if x in dic:
      dic[x] -= 1
    else:
      print('Impossible')
      break
  else:

    for x,y in dic.items():
      if y != 0:
        print('Impossible')
        break
    else:
      print('Possible')
