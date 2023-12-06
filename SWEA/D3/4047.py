t = int(input())
for tc in range(1,t+1):
  ans = []
  dic = {'S':0,'D':0,'H':0,'C':0}
  s = input()
  for i in range(0,len(s),3):
    if s[i:i+3] in ans:
      print('#{} {}'.format(tc,"ERROR"))
      break
    else:
      dic[s[i]] += 1
      ans.append(s[i:i+3])
  else:
    ss = 13 - dic['S']
    dd = 13 - dic['D']
    hh = 13 - dic['H']
    cc = 13 - dic['C']
    print('#{} {} {} {} {}'.format(tc,ss,dd,hh,cc))