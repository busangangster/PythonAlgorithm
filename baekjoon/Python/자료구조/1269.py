import sys
input = sys.stdin.readline

a,b = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
dict = {}
cnt = 0

aa = A + B
for x in aa:
  if x in dict:
    dict[x] += 1
  else:
    dict[x] = 1

for k,v in dict.items():
  if v == 1:
    cnt += 1
print(cnt)