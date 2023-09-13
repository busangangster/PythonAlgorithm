import sys
input = sys.stdin.readline

tall = []
for _ in range(9):
  tall.append(int(input()))

for i in range(9):
  for j in range(i+1,9):
    if sum(tall) - (tall[i] + tall[j]) == 100:
      ans1 = tall[i]
      ans2 = tall[j]
      break

tall.remove(ans1)
tall.remove(ans2)
tall.sort()

for x in tall:
  print(x)
