
import sys

a = int(sys.stdin.readline())

score = list(map(int,sys.stdin.readline().split()))

max_score = max(score)

print(((sum(score)/max_score*100)) / len(score))



