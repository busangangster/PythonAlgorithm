import sys
input = sys.stdin.readline

t = int(input())

for t_case in range(1,t+1):
  a,b = map(int,input().split())
  print('Case {}: {}'.format(t_case,a+b))