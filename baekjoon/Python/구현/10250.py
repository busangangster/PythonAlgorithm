import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
  h,w,n = map(int,input().split())
  first = str(n%h) # 몇층 
  second = str(n//h + 1) # 몇호인지

  if first == "0": # 나머지가 0일때를 고려 
    first = str(h)
    second = str(n//h)

  if len(second) < 2:
    second = "0"+second

  print(first+second)



  