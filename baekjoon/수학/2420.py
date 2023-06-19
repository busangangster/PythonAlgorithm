import sys
input = sys.stdin.readline

a= list(map(int,input().split()))
a.sort()

print(abs(a[1]-a[0]))