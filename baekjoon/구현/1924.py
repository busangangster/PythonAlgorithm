

import sys
input = sys.stdin.readline

a,b = map(int,input().split())
ans = 0
days = ['SUN','MON','TUE','WED','THU','FRI','SAT']

for i in range(1,a):
  if i in [1,3,5,7,8,10,12]:
    ans += 31
  elif i in [4,6,9,11]:
    ans += 30
  else:
    ans += 28

ans = ans+b
ans = ans%7
print(days[ans])


