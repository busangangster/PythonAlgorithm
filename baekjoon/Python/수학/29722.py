import sys
input = sys.stdin.readline

a = list(input().strip().split('-'))
n = int(input())
f = int(a[0])
s = int(a[1])
l = int(a[-1])
l = l + n

if l > 30: # '일'이 30을 넘어갈 경우 
  if l % 30 == 0: # 30으로 나눈 나머지가 0이라면
    s += l // 30 -1
    l = 30 # '일'은 30이 되야함. 날짜에는 0이 없기 때문에
  else:
    s += l // 30
    l = l % 30

  if s > 12: # '월'이 12를 넘어가는 경우
    if s %  12 == 0: # 나머지가 0이라면
      f += s // 12 - 1
      s = 12 # 12가 되어야 함. 날짜에는 0이 없기 때문에 
    else:
      f += s // 12
      s = s % 12

if s < 10:
  if l < 10:
    print('{}-0{}-0{}'.format(f,s,l))
    sys.exit()
  else:
    print('{}-0{}-{}'.format(f,s,l))
elif l < 10:
  print('{}-{}-0{}'.format(f,s,l))
else:
  print('{}-{}-{}'.format(f,s,l))
