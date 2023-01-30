import sys
n = int(sys.stdin.readline())
stack = []
ans =[]
cnt = 1
flag = True # flag 변수 없이 하면 no를 출력하고도 ans에 들어가있는 값들을 출력함

for _ in range(n):
  a = int(sys.stdin.readline())
  while cnt <= a:
    stack.append(cnt)
    cnt += 1
    ans.append('+')
  if stack[-1] == a:
    stack.pop()
    ans.append('-')
  else:
    print('NO')
    flag = False
    break

if flag:
  for x in ans:
    print(x)
