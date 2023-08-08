

import sys
input = sys.stdin.readline

arr= []
for _ in range(5):
  arr.append(input().strip())

ans = ["" for _ in range(len(max(arr,key=len)))] 
for x in arr:
  for i in range(len(x)):
    ans[i] += x[i]

for x in ans:
  print(x,end='')


