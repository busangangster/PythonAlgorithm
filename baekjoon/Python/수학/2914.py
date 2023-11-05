import sys
import math
input = sys.stdin.readline

a,i = map(int,input().split())
print(math.ceil(a*(i-0.99)))