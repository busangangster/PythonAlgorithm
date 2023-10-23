import sys
input = sys.stdin.readline
w = []
k = []
for _ in range(10):
  w.append(int(input()))
for _ in range(10):
  k.append(int(input()))

w.sort()
k.sort()
w_score = w[-1] + w[-2] + w[-3]
k_score = k[-1] + k[-2] + k[-3]
print(w_score,k_score)