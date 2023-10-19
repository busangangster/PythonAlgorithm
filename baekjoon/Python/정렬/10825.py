import sys
input = sys.stdin.readline

n = int(input())
grade = []
for _ in range(n):
  grade.append(list(input().split()))

grade.sort(key = lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for x in grade:
  print(x[0])