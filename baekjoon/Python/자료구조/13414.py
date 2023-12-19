import sys
input = sys.stdin.readline
dic = {}
k,l = map(int,input().split())
for _ in range(l):
  s = input().strip()
  if s in dic:
    del dic[s]
  dic[s] = 1

arr = list(dic.keys())
if len(arr) < k:
  for i in range(len(arr)):
    print(arr[i])
else:
  for i in range(k):
    print(arr[i])

