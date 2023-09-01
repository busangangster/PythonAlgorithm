import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

print(min(a),end=' ')
print(max(a))