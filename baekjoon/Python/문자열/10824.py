import sys
input = sys.stdin.readline

a,b,c,d = map(int,input().split())
k = str(a)+str(b)
t = str(c)+str(d)
print(int(k)+int(t))