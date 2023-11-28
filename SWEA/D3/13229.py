t = int(input())
dic = {"MON":1,"TUE":2,"WED":3,"THU":4,"FRI":5,"SAT":6,"SUN":7}
for tc in range(1,t+1):
  ans = 0
  s = input()
  if s == "SUN":
    ans = 7
  else:
    ans = 7 - dic[s]
  print('#{} {}'.format(tc,ans))