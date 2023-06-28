import sys
input = sys.stdin.readline

n = int(input())
days = []
ans = []
cnt = 0

for _ in range(n):
  days.append(int(input()))

first = days.pop(0)

while len(days) != 0:
  t = days[0] - first
  for i in range(1,days[-1]+1,t):
    for x in days:
      if x == i:
        days.remove(x)
  cnt +=1 

print(cnt)

  