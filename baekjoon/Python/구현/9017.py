import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  dic = {} 
  a = list(map(int,input().split()))

  for i in range(n):
    if a[i] in dic:
      dic[a[i]] += 1
    else:
      dic[a[i]] = 1
  
  nope = {}
  for k,v in dic.items():
    if v < 6:
      nope[k] = 1

  team = {}
  score = 1
  for i in range(n):
    if a[i] not in nope:
      if a[i] in team:
        if team[a[i]][0] < 4:
          team[a[i]][0] += 1
          team[a[i]][1] += score
        elif team[a[i]][0] == 4:
          team[a[i]][0] += 1
          team[a[i]][2] = score
      else:
        team[a[i]] = [1,score,0]
        
      score += 1

  team = sorted(team.items(),key = lambda x:(x[1][1], x[1][2]))
  print(team[0][0])