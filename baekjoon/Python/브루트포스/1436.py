import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
start = 666

while True:
  if '666' in str(start):
    cnt += 1
    if cnt == n:
      print(start)
      break
  start += 1