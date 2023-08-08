import sys
input = sys.stdin.readline

while True:
  a = input().strip()
  if a == '0':
    break
  else:
    for i in range(len(a)//2):
      if a[i] != a[-1-i]:
        print('no')
        break
    else:
      print('yes')



