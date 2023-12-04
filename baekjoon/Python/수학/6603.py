import sys
import itertools 
input = sys.stdin.readline

while True:
  a = list(map(int,input().split()))
  if a[0] == 0:
    break
  else:
    k = a[1:]
    ans = itertools.combinations(k,6)
    for x in ans:
      print(*x)
    print()