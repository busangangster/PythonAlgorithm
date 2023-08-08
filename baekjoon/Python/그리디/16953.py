# b에서 a를 만들어 가는 방식으로 품 

import sys

a,b = map(int,sys.stdin.readline().split())
cnt = 1

while True:
  if a == b:
    break
  elif (b%2 != 0 and b%10 != 1) or (b <a):
    cnt = -1
    break
  else:
    if b%10 == 1:
      b = b//10
      cnt += 1
    else:
      b = b//2
      cnt += 1

print(cnt)
