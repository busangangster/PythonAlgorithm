import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  a = list(input().split())
  dic = {}
  for x in a[0]:
    if x in dic:
      dic[x] += 1
    else:
      dic[x] = 1

  for x in a[1]:
    if x in dic:
      dic[x] -= 1
    else:
      dic[x] = -1

  for x in dic:
    if dic[x] != 0:
      print(a[0], '&', a[1], 'are NOT anagrams.')
      break
  else:
    print(a[0], '&', a[1], 'are anagrams.')

