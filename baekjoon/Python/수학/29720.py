import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
min_v = max(n-(m*k),0)
max_v = n - m*(k-1)-1

print(min_v,max_v)
