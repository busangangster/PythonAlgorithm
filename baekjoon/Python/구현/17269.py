import sys
input = sys.stdin.readline

dic = {'A':3,'B':2,'C':1,'D':2,'E':4,'F':3,'G':1,'H':3,'I':1,'J':1,
       'K':3,'L':1,'M':3,'N':2,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,
       'U':1,'V':1,'W':1,'X':2,'Y':2,'Z':1}

n,m = map(int,input().split())
a,b = map(str,input().split())
a = list(a)
b = list(b)
name = ''
for _ in range(min(n,m)):
  name += a.pop(0)
  name += b.pop(0)

if a:
  for i in a:
    name += i
elif b:
  for i in b:
    name += i

number = []
second = []
flag = True

for x in name:
  number.append(dic[x])

while len(number) != 2 and len(second) != 2:
  if flag == True:
    for i in range(len(number)-1):
      t = number[i] + number[i+1]
      if t >= 10:
        t = t % 10
      second.append(t)
    flag = False
    number.clear()
  else:
    for i in range(len(second)-1):
      t = second[i] + second[i+1]
      if t >= 10:
        t = t % 10
      number.append(t)
    flag = True
    second.clear()

if len(number) == 2:
  print('{}%'.format(int(''.join(map(str,number)))))
elif len(second) == 2:
  print('{}%'.format(int(''.join(map(str,second)))))