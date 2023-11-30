t = int(input())
for tc in range(1,t+1):
  a,b = map(str,input().split())
  s = list(input().split())
  ans = []
  for i in range(s.count('ZRO')):
    ans.append('ZRO')
  for i in range(s.count('ONE')):
    ans.append('ONE')
  for i in range(s.count('TWO')):
    ans.append('TWO')
  for i in range(s.count('THR')):
    ans.append('THR')
  for i in range(s.count('FOR')):
    ans.append('FOR')
  for i in range(s.count('FIV')):
    ans.append('FIV')
  for i in range(s.count('SIX')):
    ans.append('SIX')
  for i in range(s.count('SVN')):
    ans.append('SVN')
  for i in range(s.count('EGT')):
    ans.append('EGT')
  for i in range(s.count('NIN')):
    ans.append('NIN')
  
  print(a)
  print(*ans)