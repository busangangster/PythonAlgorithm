import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))

a.sort()
ans = 0

if n == 1:
  print(1)
  sys.exit()
else:
  
  if len(a) <= m:
    if abs(a[0]) >= abs(a[-1]):
      ans += abs(a[0])
      for i in a[:]:
        if i <= 0:
          a.pop(0)
    else:
      ans += abs(a[-1])
      for i in a[:]:
        if a[i] > 0:
          a.pop()

    while a:
      if len(a) == m:
        if (a[0] <0 and a[-1]) > 0:
          if abs(a[0]) >= abs(a[-1]):
            ans += ((abs(a[0]) *2) + (abs(a[-1]) * 2))
            for i in a[:]:
              if i < 0:
                a.pop(0)
          else:
            ans += ((abs(a[-1]) *2) + abs(a[0]) * 2)
            for i in a[:]:
              if i > 0:
                a.pop()

        elif a[0] <0:
          ans += abs(a[0]) *2 
          a = a[:-m]
        elif a[-1] > 0:
          ans += abs(a[-1]) * 2
          a = a[:-m]
      else:
        if abs(a[0]) >= abs(a[-1]):
          ans += abs(a[0]) * 2
          for i in a[:]:
            if i < 0:
              a.pop(0)
        else:
          ans += abs(a[-1]) * 2
          for i in a[:]:
            if i > 0:
              a.pop()
  else:
    if abs(a[0]) >= abs(a[-1]):
      ans += abs(a[0])
      a = a[m:]
      
    else:
      ans += abs(a[-1])
      a = a[:-m]
    
    while a:
      if len(a) <= m:
        if a[0] <0 and a[-1]> 0:
          ans += (abs(a[0]) * 2) + (abs(a[-1]) * 2)
        
          a = a[:-m]

        elif a[0] <0:
          ans += abs(a[0]) *2 
          a = a[:-m]
        elif a[-1] > 0:
          ans += abs(a[-1]) * 2
          a = a[:-m]
      else:
       
        if abs(a[0]) >= abs(a[-1]):
          ans += abs(a[0]) * 2
          a = a[m:]
        else:
          ans += abs(a[-1]) * 2
          a = a[:-m]


print(ans)
