import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = sorted(list(set(a)))
dic = {}

for i in range(len(b)):
  dic[b[i]] = i

for x in a:
  print(dic[x],end=' ')
