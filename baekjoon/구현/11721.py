

import sys
input = sys.stdin.readline

n = input().strip()

for i in range(0,len(n),10):
  print(n[i:i+10])
  

  