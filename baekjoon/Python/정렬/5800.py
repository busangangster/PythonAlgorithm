import sys
input = sys.stdin.readline

n = int(input())
for x in range(n):
  a = list(map(int,input().split()))
  t = a[1:]

  t.sort()
  gap = []
  for i in range(len(t)-1):
    gap.append(abs(t[i]-t[i+1]))

  print('Class %s' %(x+1))
  print('Max %s, Min %s, Largest gap %s' %(t[-1],t[0],max(gap)))

