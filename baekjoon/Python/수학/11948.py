import sys
input = sys.stdin.readline

k = [int(input()) for _ in range(6)]
t = k[0:4]
j = k[4:]
t.sort(reverse=True)
j.sort(reverse=True)
print(sum(t[:3]) + j[0])