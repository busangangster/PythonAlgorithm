import sys
input = sys.stdin.readline
score = [int(input()) for _ in range(10)]
ans = 0
result = float('inf')
answer = 0
for x in score:
  ans += x
  k = abs(100-ans)
  if k <= result:
    result = k
    answer = ans
print(answer)