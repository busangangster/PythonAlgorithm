t = int(input())
for tc in range(1,t+1):
  a = list(map(int,input().split()))
  tmp = 0
  for x in a:
    if x < 40:
      tmp += 40
    else:
      tmp += x
  print("#{} {}".format(tc,tmp//len(a)))