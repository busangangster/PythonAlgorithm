
def is_promising(x):
  for i in range(x):
    if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
      return False
  return True

def check(x):
  global ans
  if x == n:
    ans += 1
    return 
  
  for i in range(n):
    row[x] = i
    if is_promising(x):
      check(x+1)
    
t = int(input())
for tc in range(1,t+1):
  n = int(input())
  ans = 0
  row = [0] * n
  check(0)
  print('#{} {}'.format(tc,ans))