import sys
input = sys.stdin.readline

arr = []
x,y,w,h = map(int,input().split())

arr.append(abs(0-x))
arr.append(abs(0-y))
arr.append(w-x)
arr.append(h-y)

print(min(arr))