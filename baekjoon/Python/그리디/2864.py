import sys
input = sys.stdin.readline

a = list(input().split())
t = ''
k = ''
mini = 0
maxi = 0

for x in a[0]: 
  if x == '5':
    t += '6'
  else:
    t += x

for x in a[1]:
  if x == '5':
    k += '6'
  else:
    k += x

maxi = int(t) + int(k)

t = ''
k = ''

for x in a[0]: 
  if x == '6':
    t += '5'
  else:
    t += x

for x in a[1]:
  if x == '6':
    k += '5'
  else:
    k += x

mini = int(t)+int(k)

print(mini,maxi)