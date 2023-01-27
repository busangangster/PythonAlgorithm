import sys
s = int(sys.stdin.readline())
cnt = 0
sum = 0

while True:
  cnt += 1
  sum += cnt
  if sum > s:
    break
print(cnt-1)
'''
n = 1

while n*(n+1)/2 <= s:
  n +=1

print(n-1)
'''

  