t = int(input())
grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for t_case in range(1,t+1):
  n,k = map(int,input().split())
  score = []
  ans = []
  for i in range(1,n+1):
    total = 0
    a,b,c = map(int,input().split())
    total = (a*0.35) + (b*0.45) + (c*0.2)
    score.append([i,round(total,2)])
  score.sort(key = lambda x:x[1],reverse=True)

  for i in range(10):
    for j in range(n//10):
      ans.append(grade[i])

  for i in range(n):
    if score[i][0] == k:
      t = i

  print('#{} {}'.format(t_case,ans[t]))