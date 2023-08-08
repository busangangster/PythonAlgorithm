import sys
input = sys.stdin.readline

n,a,d = map(int,input().split())

arr = list(map(int,input().split()))
hmm = []

for i in arr:
  if i in hmm:
    continue
  else:
    if i == a:
      hmm.append(i)
    if hmm and hmm[-1] + d == i:
      hmm.append(i)

print(len(hmm))