import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  robo = []
  for _ in range(5):
    robo.append(list(input().strip()))

  tt = len(robo[0])
  RSP = []
  for i in range(tt):
    for j in range(len(robo)):
      if robo[j]:
        RSP.append(robo[j].pop(0))

    print(RSP)
    if len(RSP) >= 3:
      if 'R' in RSP and 'S' in RSP and 'P' in RSP:
        print('f')
        RSP.clear()
        
      elif 'P' not in RSP:
        for p in range(len(RSP))[:]:
          if RSP[p] == 'S':
            print('s')
            robo[p].clear()
            print(robo)
        RSP.clear()

      elif 'R' not in RSP:
        for p in range(len(RSP)):
          if RSP[p] == 'P':
            print('t')
            robo[p].clear()
        RSP.clear()

      elif 'S' not in RSP:
        for p in range(len(RSP)):
          if RSP[p] == 'R':
            print('fou')
            robo[p].clear()
        RSP.clear()

    elif len(RSP) == 2:
      if RSP[0] == RSP[1]:
        RSP.clear()
        continue
      # elif (RSP[0],RSP[1]) in (('S','P'),('R','S'),('P','R')):
  

    