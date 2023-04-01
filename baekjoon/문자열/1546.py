
import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
ans = []

m = max(a)

for i in a:
  t1 = i/m*100
  ans.append(t1)

print(sum(ans)/len(ans))


# import sys

# a = int(sys.stdin.readline())

# score = list(map(int,sys.stdin.readline().split()))

# max_score = max(score)

# print(((sum(score)/max_score*100)) / len(score))




