import sys

score = 0
credits = 0

grade = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,
         'D+':1.5,'D0':1.0,'F':0.0}

for _ in range(20):
  a = list(sys.stdin.readline().split())
  a[1] = float(a[1])
  if a[2] != 'P':
    score += a[1] * grade[a[2]]
    credits += a[1]

print(score/credits)


