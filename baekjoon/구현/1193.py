import sys
input = sys.stdin.readline

n = int(input())
line = 1

while n > line:
  n -= line
  line += 1

if line %2 == 0: # 짝수 라인
  top = n
  bottom = line -n +1
else: # 홀수 라인 
  top = line -n +1
  bottom = n

print('%d/%d' %(top,bottom))
