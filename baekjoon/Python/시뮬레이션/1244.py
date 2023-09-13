import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
m = int(input())
a.insert(0,10)

def switch(num):
  if a[num] == 0:
    a[num] = 1
  else:
    a[num] = 0
  return

for _ in range(m):
  g,s = map(int,input().split())
  if g == 1:
    for i in range(s,n+1,s):
      switch(i)

  else:
    switch(s)
    for i in range(n//2):
      if s + i > n or s - i < 0:
        break
      if a[s+i] == a[s-i]:
        switch(s+i)
        switch(s-i)
      else:
        break

for i in range(1,len(a)+1,20):
  print(*a[i:i+20])