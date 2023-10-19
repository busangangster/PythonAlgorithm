import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
a = set(a)
b = list(a)
b.sort()
print(*b)