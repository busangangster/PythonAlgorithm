t = int(input())
for t_case in range(1,t+1):
  n = int(input())
  s = ''
  for _ in range(n):
    a,b = map(str,input().split())
    for _ in range(int(b)):
      s += a
  print('#{}'.format(t_case))
  
  for i in range(0,len(s),10): # 10개씩 끊어서 출력 
    print(s[i:i+10])
