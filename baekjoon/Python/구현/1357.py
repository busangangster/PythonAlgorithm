import sys
input = sys.stdin.readline

def Rev(x):
  x = list(str(x))
  r = x[::-1]
  ans = ''.join(map(str,r))
  return int(ans)

a,b = map(int,input().split())
print(Rev(Rev(a)+Rev(b)))