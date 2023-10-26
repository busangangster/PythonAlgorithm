import sys
input = sys.stdin.readline

def pal(s,l,r):
  global cnt
  if l >= r:
    return 1
  elif s[l] != s[r]:
    return 0
  else:
    cnt += 1
    return pal(s,l+1,r-1)


n = int(input())
for _ in range(n):
  a = input().strip()
  cnt = 1
  print(pal(a,0,len(a)-1),cnt)
