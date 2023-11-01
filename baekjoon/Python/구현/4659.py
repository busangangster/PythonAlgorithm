import sys
input = sys.stdin.readline

m = ['a','e','i','o','u']
b = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v',
     'w','x','y','z']

while True:
  a = input().strip()
  flag = True
  cnt = 0
  if a == 'end':
    break
  else:
    for x in m:
      if x in a:
        cnt += 1

    if cnt == 0:
      flag = False

    if len(a) >= 3:
      for i in range(len(a)-2):
        if (a[i] in m and a[i+1] in m and a[i+2] in m) or (a[i] in b and a[i+1] in b and a[i+2] in b):
          flag = False
          break

    for i in range(len(a)-1):
      if a[i] == a[i+1]:
        if (a[i] == 'e' and a[i+1] == 'e') or (a[i] == 'o' and a[i+1] == 'o'):
          continue
        else:
          flag = False
          break

  if flag == False:
    print('<{}> is not acceptable.'.format(a))
  else:
    print('<{}> is acceptable.'.format(a))