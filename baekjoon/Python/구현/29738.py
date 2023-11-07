import sys
input = sys.stdin.readline
t = int(input())

for t_case in range(1,t+1):
  n = int(input())
  if n > 4500:
    print('Case #{}: Round 1'.format(t_case))
  elif 4500 >= n > 1000:
    print('Case #{}: Round 2'.format(t_case))
  elif 1000 >= n > 25:
    print('Case #{}: Round 3'.format(t_case))
  elif n <= 25:
    print('Case #{}: World Finals'.format(t_case))